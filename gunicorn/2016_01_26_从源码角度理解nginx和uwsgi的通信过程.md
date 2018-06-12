# 从源码角度理解nginx和uwsgi的通信过程

2016年01月26日 08:59:50

>  [fangjian1204的专栏](https://blog.csdn.net/fangjian1204)

**问题来源**

曾经遇到过一个项目涉及到了上传商品图片的问题，而我在限制图片大小的时候，是先把整个图片都读取到内存中，然后再判断其大小。这种做法当出现恶意攻击或者图片很大时，会严重影响web application的性能。原先想通过先判断首部的content-length来对大小进行限制。但后来觉得，如果图片是先由前端的nginx完全读取后再转发给uwsgi的，那这样判断依然会影响nginx的性能。为此，我查看了nginx的源码，找到了nginx和uwsgi的通信过程，下面是整个通信的具体流程。

**设置回调函数**

我们知道，nginx把浏览器等发过来的请求通过proxy_pass或者uwsgi_pass转发给上游的web application进行处理，然后把处理的结果发送给浏览器。uwsgi_pass命令的处理函数为ngx_http_uwsgi_handler,也就是说，当有请求到达配置uwsgi_pass的location时，会调用ngx_http_uwsgi_handler方法，而该方法是整个uwsgi事件处理的入口方法。下面来看该方法：

```
static ngx_int_t ngx_http_uwsgi_handler(ngx_http_request_t *r)
{
    ngx_http_upstream_t *u;
    ngx_http_uwsgi_loc_conf_t   *uwcf;
    uwcf = ngx_http_get_module_loc_conf(r, ngx_http_uwsgi_module);
    u = r->upstream;
    ……
    u->create_request = ngx_http_uwsgi_create_request;//根据wsgi协议创建请求包体
    u->process_header = ngx_http_uwsgi_process_status_line;//根据wsgi协议解析uwsgi发送来的头部
    ……
    rc = ngx_http_read_client_request_body(r, ngx_http_upstream_init);//从浏览器读取body数据
    ……
}
```

该方法的首先创建一个ngx_http_upstream_t 结构体，然后设置该结构体的几个回调函数。nginx是一个高度模块化的web server，每一个功能都是通过一个模块来实现的，和uwsgi的通信也不例外。整个通信过程是在都是由ngx_http_uwsgi_module.c这个模块文件实现的。当然，要想把每一个模块添加到nginx中，必须要有一些钩子，在nginx中就是一些链表，然后把每一个模块的处理方法添加到这些链表中，这样就会被nginx框架代码逐一调用。而与web application通信的的钩子文件就是ngx_http_upstream.c文件，至于nginx是在何时触发这些钩子函数的，简单的说就是把这些钩子函数赋值给epoll的读写事件，当有读写请求时，epoll的事件响应机制就会调用这些钩子函数。大家可以看到，上面的钩子函数，只有构造请求体，解析响应头部，确没有对包体的处理，这是因为，nginx根本不需要对包体进行处理，只是简单的存储转发。

**从浏览器读取数据**

首先看nginx如何决定需要从浏览器读取多少数据，这个很明显是由content-length首部决定的，但也会受到client_max_body_size指令的影响。我们可以在nginx.conf中添加**client_max_body_size**配置指令，该指令可以放在http、server和location三个地方。nginx读取完头部之后，会调用src/http/ngx_http_core_module.c文件中ngx_http_core_find_config_phase方法去根据重写后的URI检索出匹配的location块，此时配置文件已经合并完成，只是简单的检索。如果发现配置了client_max_body_size配置文件，则会通过下面的比较来判断请求体是否超过给定的大小：

```
ngx_int_t ngx_http_core_find_config_phase(ngx_http_request_t *r, ngx_http_phase_handler_t *ph)
{
    if (clcf->client_max_body_size < r->headers_in.content_length_n)
    {
      ngx_log_error(NGX_LOG_ERR, r->connection->log, 0,"client intended to send too large body: %O bytes",
            r->headers_in.content_length_n);
    }
}
```

如果没有超过设定的大小，那么就把ngx_http_request_body_t结构体中rest设置为content-length的大小，表示需要读取的字节数。 
下面我们来看看真正的读取方法ngx_http_read_client_request_body，该方法传入了一个回调函数ngx_http_upstream_init，而该回调函数就是开启nginx和上游通信的入口。注意，虽然ngx_http_read_client_request_body方法不会阻塞，即当没有数据接收时会立即返回，但是，只有当数据全部接收完毕，才会调用ngx_http_upstream_init方法，具体的实现我们来看代码：

```
ngx_int_t  ngx_http_read_client_request_body(ngx_http_request_t *r, ngx_http_client_body_handler_pt post_handler) 
{
    if (rb->rest == 0) { /* 已经全部接收完body */
        if (r->request_body_in_file_only) {
            ngx_http_write_request_body(r)； /* 把缓冲区的数据写入文件 */
        }
        post_handler(r); /* 调用回调函数，即ngx_http_upstream_init */
    }
    r->read_event_handler = ngx_http_read_client_request_body_handler;//设置读事件
    rc = ngx_http_do_read_client_request_body(r);
}
```

由此可以看出，如果读取完毕，则调用ngx_http_upstream_init开始和uwsgi进行通信，如果没有，则首先把读事件设置为ngx_http_read_client_request_body_handler方法，该方法内部除了做一些错误检查，还是仍然调用ngx_http_read_client_request_body方法，也就是说只要没读取完所有的body，nginx会通知epoll一直调用本方法进行body的读取操作。在该方法的最后，调用ngx_http_do_read_client_request_body方法进行真正的读取操作。

```
static ngx_int_t  ngx_http_do_read_client_request_body(ngx_http_request_t *r) 
{
    for ( ;; ) {
        for ( ;; ) {
            if (rb->buf->last == rb->buf->end) { /* 请求的request_body成员中的buf缓冲区已写满 */
                rc = ngx_http_request_body_filter(r, &out);/* 对数据进行过滤并把数据移入请求体缓存中，如果空间不够，则存入临时文件 */
            }

            n = c->recv(c, rb->buf->last, size); //从套接字缓冲区读取包体到缓冲区中
            if (rb->rest == 0) { //已经接收到了完整的包体
                break;
            }
        }
    }
    if (rb->temp_file || r->request_body_in_file_only) {
        ngx_http_write_request_body(r)； //把数据移入请求体缓存中，如果空间不够，则存入临时文件
    }
    if (!r->request_body_no_buffering) { //nginx可以通过proxy_request_buffering关闭缓存
        r->read_event_handler = ngx_http_block_reading;
        rb->post_handler(r);//调用ngx_http_upstream_init方法
    }
    return NGX_OK;
}
```

从上面可以看到，如果开启了**proxy_request_buffering**(默认开启)，则nginx是把所有的数据都读取到之后，再发送给uwsgi。

**发送数据给uwsgi**

下面看整个通信的入口函数ngx_http_upstream_init：

```
void  ngx_http_upstream_init(ngx_http_request_t *r) 
{
    ngx_http_upstream_init_request(r);
}

static void ngx_http_upstream_init_request(ngx_http_request_t *r)
{
    u->create_request(r)；//调用ngx_http_uwsgi_create_request创建请求包体
    ngx_http_upstream_connect(r, u);//建立和uwsgi的连接
}
```

在ngx_http_uwsgi_create_request方法中，主要的工作就是根据wsgi协议构建请求报文，主要是首部信息，然后通过建立的连接把报文发送给uwsgi。在方法ngx_http_upstream_connect中，设置了和uwsgi通信的方法：

```
static void  ngx_http_upstream_connect(ngx_http_request_t *r, ngx_http_upstream_t *u)  
{
    ……
    rc = ngx_event_connect_peer(&u->peer); //真正进行请求建立连接工作
    u->write_event_handler = ngx_http_upstream_send_request_handler; //设置向uwsgi发送请求的方法
    u->read_event_handler = ngx_http_upstream_process_header; //设置接收uwsgi请求的方法
    ……
    ngx_http_upstream_send_request(r, u, 1); //调用该方法向上游服务器发送请求
}
```

**从uwsgi读取头部信息**

由此可知，当从uwsgi发送数据到nginx时，会触发读事件，即调用ngx_http_upstream_process_header方法：

```
static void  ngx_http_upstream_process_header(ngx_http_request_t *r, ngx_http_upstream_t *u) 
{
    for ( ;; ) {
        n = c->recv(c, u->buffer.last, u->buffer.end - u->buffer.last); //从uwsgi接收头部数据
        if (n == NGX_AGAIN) { //如果数据不够，则继续加入epoll中
            ngx_handle_read_event(c->read, 0)；
        }
        rc = u->process_header(r); //调用uwsgi设置的回调函数ngx_http_uwsgi_process_status_line解析状态吗和头部
        if (rc == NGX_AGAIN) { //接收的数据不够，继续读取
         continue;
         }
        break;
    }
    /* rc == NGX_OK：解析到完整的包头 */
    if (!r->subrequest_in_memory) {
        ngx_http_upstream_send_response(r, u);//开始转发响应头部给客户端
        return;
    }
}
```

解析完头部信息后，就会调用ngx_http_upstream_process_header中最后的ngx_http_upstream_send_response方法发送响应头给客户端。另外在该方法中，就会涉及到用户在配置uwsgi时，是否开启接收**uwsgi_buffering**标志(默认开启)。如果开启，则nginx会尽可能多的把数据缓存下来再发送给浏览器，如果内存缓存不够，则会存入临时文件；如果被用户关闭，则nginx最多只缓存uwsgi_buffer_size大小的body，当缓存满时，会导致后端基于阻塞模型的uwsgi无法send而阻塞。下面分别讨论这两种情况下的数据传输。

**未开启缓存的情况下从uwsgi读取包体并转发**

在uwsgi_buffering设置为off的情况下，从uwsgi读取body和发送body给浏览器的方法分别为ngx_http_upstream_process_non_buffered_upstream和ngx_http_upstream_process_non_buffered_downstream。而这两个方法内部都是调用了ngx_http_upstream_process_non_buffered_request方法，下面具体来看该方法：

```
static void ngx_http_upstream_process_non_buffered_request(ngx_http_request_t *r,ngx_uint_t do_write)
{
    /* 这是在一个大循环中执行的，也就是说，与上下游间的通信可能反复执行，即接收一点，发送一点 */
    for ( ;; ) 
    {
        if (do_write)//向下游发送响应
        {
            if (u->out_bufs || u->busy_bufs) 
            {
                /* 向下游发送out_bufs指向的内容*/
                rc = ngx_http_output_filter(r, u->out_bufs);

            }
            // 到目前为止需要向下游转发的响应包体都已经全部发送完了
            if (u->busy_bufs == NULL) 
            {
                b->pos = b->start;
                b->last = b->start;
            }
        }
        /* do_write为0，表示需要由上游读取响应 */
        size = b->end - b->last;//获取buffer缓冲区中还有多少剩余空间
        if (size && upstream->read->ready) 
        {
            n = upstream->recv(upstream, b->last, size);//将上游的响应接收到buffer缓冲区中
            if (n == NGX_AGAIN) 
            {//期待epoll下次有读事件时再继续调度
                break;
            }
            if (n > 0) 
            {
                u->state->response_length += n;
                /* 处理包体 */
                u->input_filter(u->input_filter_ctx, n)；
            }
            /* 读取到来自上游的响应，这时设置do_write为1，准备向下游转发刚收到的响应 */
            do_write = 1;
            continue;
        }
        break;
    }
}
```

可以看到，该方法是读一些数据就设置do_write=1，从而触发发送事件，因此是非缓存的。

**开启缓存的情况下从uwsgi读取包体并转发**

在uwsgi_buffering设置为on的情况下，从uwsgi读取body和发送body给浏览器的方法分别为ngx_http_upstream_process_upstream 和 ngx_http_upstream_process_downstream。而这两个方法最后都是调用ngx_event_pipe方法，在该方法中，通过标志位来分别从uwsgi读取数据和向浏览器发送数据，具体如下：

```
ngx_int_t ngx_event_pipe(ngx_event_pipe_t *p, ngx_int_t do_write)
{
    for ( ;; ) 
    {
        if (do_write) 
        {
            rc = ngx_event_pipe_write_to_downstream(p);//向下游客户端发送响应包体
        }
        p->read = 0;
        p->upstream_blocked = 0;   
        /* 读取上游服务器的响应 */
        ngx_event_pipe_read_upstream(p);
        if (!p->read && !p->upstream_blocked) {
            break;
        }
        /* 当读取完所有的包体后，会把p->read设置为1，从而导致do_write为1，即开始发送数据给浏览器 */
        do_write = 1;
    }
}
```

从uwsgi读取数据：在这个过程中会涉及以下几种情况：1)接收响应头部时可能接收到部分包体；2)如果没有达到bufs.num上限，那么可以分配bufs.size大小的内存块充当接收缓冲区；4)如果缓冲区全部写满，则应该写入临时文件：

```
static ngx_int_t ngx_event_pipe_read_upstream(ngx_event_pipe_t *p)
{

    for ( ;; ) 
    {
            /* 从缓冲区链表中取出一块ngx_buf_t缓冲区 */ 
            if (p->free_raw_bufs) 
            {
                chain = p->free_raw_bufs;
            } 
            //缓冲区已空，尝试继续分配缓冲区
            else if (p->allocated < p->bufs.num) 
            {
                b = ngx_create_temp_buf(p->pool, p->bufs.size);//可以从内存池中分配到一块新的缓冲区
                ……
            }
            //缓存区已满
            else if (p->cacheable|| p->temp_file->offset < p->max_temp_file_size)
            {
                rc = ngx_event_pipe_write_chain_to_temp_file(p);//将响应文件写入临时文件中

            } else {

                break;
            }
            //接收上游的响应
            n = p->upstream->recv_chain(p->upstream, chain);
    }
    if (p->length == 0) {//数据接收完毕，开发发送数据给浏览器
        p->upstream_done = 1;
        p->read = 1;
    }
}
```

可以看到该方法是尽可能多的把数据缓存下来再发送给浏览器。

**总结**

1. nginx发送数据到uwsgi：首先nginx会判断用户是否设置client_max_body_size指令，如果设置了，则会用该值来和content-length进行比较，如果发送的包体超过了设置的值，则nginx返回413包体过大的错误。如果包体在给定范围内，则nginx会根据proxy_request_buffering是否开启，来决定是否先缓存客户端发来的请求。如果关闭了proxy_request_buffering(默认开启)，则nginx是接收到一部分数据就直接发送给uwsgi；如果开启了proxy_request_buffering，则nginx是是把所有的数据都读取到之后，再发送给uwsgi，如果body过大，则可能需要把body先存入临时文件中。
2. uwsgi返回数据到nginx：如果uwsgi_buffering开启(默认开启)，nginx会尽可能缓存uwsgi发送来的body，缓冲区的大小由uwsgi_buffers和uwsgi_buffer_size两个指令设置的缓冲区之和；如果还是存不下，则需要写入临时文件，临时文件的大小由uwsgi_max_temp_size和uwsgi_temp_file_write_size决定；如果关闭，则数据同步的发送给浏览器，每次最多缓存uwsgi_buffer_size的数据，可以从upstream->recv()方法看出，如果满了，会导致uwsgi无法发送数据而阻塞。
3. 在工作中，一般是保持proxy_request_buffering和uwsgi_buffering默认开启的设置，这样才能充分利用nginx高并发的特性，不会让一个连接长时间占用后端的web application；另外如果要限制请求body的大小，如上传图片，一般是nginx开到最大合理的大小，然后python按照具体接口的业务，读一部分，超过大小就扔掉。因为nginx可能需要限制多个请求body的大小，所以一般设置一个最大值，然后在web应用中根据需求来加以限制。
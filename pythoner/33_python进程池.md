# [python进程池](https://www.cnblogs.com/zhangfengxian/p/python-process-pool.html)

当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态成生多个进程，但如果是上百甚至上千个目标，手动的去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。

初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务，请看下面的实例：

```
Copyimport multiprocessing
import time
import os
import random


def test1(msg):
        t_start = time.time()   
        print("%s开始执行，进程号为%d" % (msg, os.getpid()))
        time.sleep(random.random() * 2)  
        t_stop = time.time()
        print("%s执行完成，耗时%.2f" % (msg, t_stop - t_start)) 


if __name__ == "__main__":
    
        po = multiprocessing.Pool(3)
        for i in range(0, 10):
                # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
                # 每次循环将会用空闲出来的子进程去调用目标
                po.apply_async(test1, (i,))
    
        print("-----start-----")
    
        po.close() # 关闭进程池，关闭后po不再接收新的请求
        po.join() # 等待po中所有子进程执行完成，必须放在close语句之后

        print("-----end-----")
```

运行结果：

```
Copy-----start-----
0开始执行，进程号为40291
1开始执行，进程号为40292
2开始执行，进程号为40293
2执行完成，耗时0.59
3开始执行，进程号为40293
0执行完成，耗时1.21
4开始执行，进程号为40291
1执行完成，耗时1.56
5开始执行，进程号为40292
3执行完成，耗时1.58
6开始执行，进程号为40293
5执行完成，耗时1.36
7开始执行，进程号为40292
4执行完成，耗时1.73
8开始执行，进程号为40291
6执行完成，耗时1.34
9开始执行，进程号为40293
8执行完成，耗时0.71
9执行完成，耗时0.36
7执行完成，耗时1.21
-----end-----
```

multiprocessing.Pool常用函数解析：

- apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
- close()：关闭Pool，使其不再接受新的任务；
- terminate()：不管任务是否完成，立即终止；
- join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；

## 进程池中的Queue[#](https://www.cnblogs.com/zhangfengxian/p/python-process-pool.html#%E8%BF%9B%E7%A8%8B%E6%B1%A0%E4%B8%AD%E7%9A%84queue)

如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()，否则会得到一条如下的错误信息：

RuntimeError: Queue objects should only be shared between processes through inheritance.

下面的实例演示了进程池中的进程如何通信：

```
Copyimport os
import multiprocessing
import time


def write(q):
        print("write启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
        for i in "python":
                q.put(i)


def read(q):
        print("read启动(%s)，父进程为(%s)" % (os.getpid(), os.getppid()))
        for i in range(q.qsize()):
                print("read从Queue获取到消息：%s" % q.get(True))    


if __name__ == "__main__":
        print("(%s) start" % os.getpid())
        q = multiprocessing.Manager().Queue()
        po = multiprocessing.Pool()
        po.apply_async(write, args=(q,))

        time.sleep(2)   
    
        po.apply_async(read, args=(q,))
        po.close()
        po.join()
    
        print("(%s) end" % os.getpid())                                    
```

运行结果：

```
Copy(41888) start
write启动(41894)，父进程为(41888)
read启动(41895)，父进程为(41888)
read从Queue获取到消息：p
read从Queue获取到消息：y
read从Queue获取到消息：t
read从Queue获取到消息：h
read从Queue获取到消息：o
read从Queue获取到消息：n
(41888) end
```

作者：[ 张风闲](http://blog.esofar.cn/)

出处：<https://www.cnblogs.com/zhangfengxian/p/python-process-pool.html>

本站使用「[CC BY 4.0](https://creativecommons.org/licenses/by/4.0)」创作共享协议，转载请在文章明显位置注明作者及出处。
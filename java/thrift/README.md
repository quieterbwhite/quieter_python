# thrift 使用

## 安装
```
详见本目录安装文档
```

## 编写 .thrift 文件
```
详见代码中的示例
```

## 生成对应代码
```
thrift --gen java src/thrift/data.thrift

thrift --gen py src/thrift/data.thrift

将生成的thrift目录拷贝到源码目录 src/main/java 下
```

## 安装代码中的依赖
```
如:
    search.maven.org 搜索 libthrift
```

## 编写客户端和服务端的代码
```
见示例
```

## Thrift 传输格式
```
TBinaryProtocol - 二进制格式
TCompactProtocol - 压缩格式
TJSONProtocol - JSON格式
TSimpleJSONProtocol - 提供JSON只写协议，生成的文件很容易通过脚本语言解析
TDebugProtocol - 使用易懂的可读的文本格式，以便于debug
```

## Thrift 传输方式
```
TSocket - 阻塞式socket

    用的最少，效率最低, 相当于 java 中的 ServerSocket

TFramedTransport - 以frame为单位进行传输，非阻塞式服务中使用

    
TFileTransport - 以文件形式进行传输

    
TMemoryTransport - 将内存用于I/O, Java实现时内部实际使用了简单的ByteArrayOutputStream

    
TZlibTransport - 使用zlib进行压缩，与其他传输方式联合使用。当前无Java实现。
```

## Thrift 支持的服务模型
```
TSimpleServer - 简单的单线程服务模型，常用于测试

TThreadPoolServer - 多线程服务模型，使用标准的阻塞式IO

TNonblockingServer - 多线程服务模型，使用非阻塞式IO（需使用TFramedTransport数据传输方式）

THsHaServer - THsHa引入了线程池去处理， 其模型把读写任务放到线程池去处理；

    Half-sync / Half-async 的处理模式， Half-async是在处理IO事件上(accept/read/write io)
    Half-sync 用于handler对rpc的同步处理
```


# java SE Lesson 14

```
输入流
```

```
读数据的逻辑为:

open a stream
while more information
read information
close the stream
```

```
流的分类

节点流: 从特定的地方读写的流类，如磁盘或一块内存区域

过滤流：使用节点流作为输入或输出。过滤流是使用一个已经存在的输入流或输出流连接创建的。
```

```
InputStream

FileInputStream
ByteArrayInputStream
FilterInputStream    过滤流
ObjectInputStream
PipedInputStream
SequenceInputStream
StringBufferInputStream
```

```
FilterInputStream, 过滤流

DataInputStream
BufferedInputStream
LineNumberInputStream
PushbackInputStream

过滤流会包装其他节点流
```

```
OutputStream

FileOutStream
ByteArrayOutputStream
FilterOutputStream
ObjectOutputStream
PipedOutputStream
```

```
FilterOutputStream

DataOutputStream
BufferedOutputStream
PrintStream
```

```
装饰器模式可以在不创造更多子类的情况下扩展对象的功能。
是动态的给一个对象增加功能，而不是像继承是给类增加功能。

客户端并不会觉得对象在装饰前和装饰后有什么不同
```

```
装饰器模式的角色

抽象构建角色
具体构建角色
装饰角色
具体装饰角色 
```

```
代码 lesson14
```

```
RandomAccessFile
随机访问文件类
```


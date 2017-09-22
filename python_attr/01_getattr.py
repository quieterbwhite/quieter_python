Python中的getattr()函数详解

ref: http://www.cnblogs.com/pylemon/archive/2011/06/09/2076862.html

函数本身的doc

getattr(object, name[, default]) -> value

Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y. 
When a default argument is given, it is returned when the attribute doesn't 
exist; without it, an exception is raised in that case.

告诉我这个函数的作用相当于是

object.name

试了一下getattr(object,name)确实和object.name是一样的功能.只不过这里可以把name作为一个变量去处理

书上的例子很好的说明了这个函数的功用

使用getattr可以轻松实现工厂模式。

例：一个模块支持html、text、xml等格式的打印，根据传入的formate参数的不同，调用不同的函数实现几种格式的输出

import statsout  
def output(data, format="text"):                            
    output_function = getattr(statsout, "output_%s" %format)  
    return output_function(data)
这个例子中可以根据传入output函数的format参数的不同 去调用statsout模块不同的方法(用格式化字符串实现output_%s)

返回的是这个方法的对象 就可以直接使用了 如果要添加新的格式 只需要在模块中写入新的方法函数 在调用output函数时使用新的参数就可以使用不同的格式输出

确实很方便

 

为了加深对getattr函数的理解 转载一篇英文的说明

Python’s getattr function is used to fetch an attribute from an object, using a string object instead of an identifier to identify the attribute. In other words, the following two statements are equivalent:

value = obj.attribute
value = getattr(obj, "attribute")
If the attribute exists, the corresponding value is returned. If the attribute does not exist, you get an AttributeError exception instead.

The getattr function can be used on any object that supports dotted notation (by implementing the __getattr__ method). This includes class objects, modules, and even function objects.

path = getattr(sys, "path")
doc = getattr(len, "__doc__")
The getattr function uses the same lookup rules as ordinary attribute access, and you can use it both with ordinary attributes and methods:

result = obj.method(args)

func = getattr(obj, "method")
result = func(args)
or, in one line:

result = getattr(obj, "method")(args)
Calling both getattr and the method on the same line can make it hard to handle exceptions properly. To avoid confusing AttributeError exceptions raised by getattr with similar exceptions raised inside the method, you can use the following pattern:

try:
    func = getattr(obj, "method")
except AttributeError:
    ... deal with missing method ...
else:
    result = func(args)
The function takes an optional default value, which is used if the attribute doesn’t exist. The following example only calls the method if it exists:

func = getattr(obj, "method", None)
if func:
    func(args)
Here’s a variation, which checks that the attribute is indeed a callable object before calling it.

func = getattr(obj, "method", None)
if callable(func):
    func(args)



setattr(object, name, value)

    This is the counterpart(相对) of getattr(). The arguments

    are an object, a string and an arbitrary(任意的) value. The string may name an existing

    attribute or a new attribute. The function assigns the value to the attribute,

    provided the object allows it. For example, setattr(x,'foobar', 123) is equivalent to x.foobar = 123.


delattr(object, name)

    This is a relative of setattr(). The arguments are

    an object and a string. The string must be the name of one of the object’s

    attributes. The function deletes the named attribute, provided the object allows

    it. For example, delattr(x, 'foobar') is equivalent to del x.foobar.


hasattr用于确定一个对象是否具有某个属性。

    语法：

    hasattr(object, name) -> bool

    判断object中是否有name属性，返回一个布尔值。



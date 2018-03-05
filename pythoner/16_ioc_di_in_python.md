# IOC & DI in Python
> https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python  
> https://blog.tonyseek.com/post/notes-about-ioc-and-di/  
> https://www.reddit.com/r/Python/comments/3xtcmg/inversion_of_control_dependency_injection_in/  
> https://lostechies.com/ryansvihla/2009/11/16/i-recant-my-ioc-ioc-containers-in-dynamic-languages-are-silly/  

## Why is IoC / DI not common in Python?
```
In Java IoC / DI is a very common practice which is extensively used in web applications, nearly all available frameworks and Java EE. On the other hand, there are also lots of big Python web applications, but beside of Zope (which I've heard should be really horrible to code) IoC doesn't seem to be very common in the Python world. (Please name some examples if you think that I'm wrong).

There are of course several clones of popular Java IoC frameworks available for Python, springpython for example. But none of them seems to get used practically. At least, I've never stumpled upon a Django or sqlalchemy+<insert your favorite wsgi toolkit here> based web application which uses something like that.

In my opinion IoC has reasonable advantages and would make it easy to replace the django-default-user-model for example, but extensive usage of interface classes and IoC in Python looks a bit odd and not »pythonic«. But maybe someone has a better explanation, why IoC isn't widely used in Python.

Answer:

I don't actually think that DI/IoC are that uncommon in Python. What is uncommon, however, are DI/IoC frameworks/containers.

Think about it: what does a DI container do? It allows you to

wire together independent components into a complete application ...
... at runtime.
We have names for "wiring together" and "at runtime":

scripting
dynamic
So, a DI container is nothing but an interpreter for a dynamic scripting language. Actually, let me rephrase that: a typical Java/.NET DI container is nothing but a crappy interpreter for a really bad dynamic scripting language with butt-ugly, sometimes XML-based, syntax.

When you program in Python, why would you want to use an ugly, bad scripting language when you have a beautiful, brilliant scripting language at your disposal? Actually, that's a more general question: when you program in pretty much any language, why would you want to use an ugly, bad scripting language when you have Jython and IronPython at your disposal?

So, to recap: the practice of DI/IoC is just as important in Python as it is in Java, for exactly the same reasons. The implementation of DI/IoC however, is built into the language and often so lightweight that it completely vanishes.

(Here's a brief aside for an analogy: in assembly, a subroutine call is a pretty major deal - you have to save your local variables and registers to memory, save your return address somewhere, change the instruction pointer to the subroutine you are calling, arrange for it to somehow jump back into your subroutine when it is finished, put the arguments somewhere where the callee can find them, and so on. IOW: in assembly, "subroutine call" is a Design Pattern, and before there were languages like Fortran which had subroutine calls built in, people were building their own "subroutine frameworks". Would you say that subroutine calls are "uncommon" in Python, just because you don't use subroutine frameworks?)

BTW: for an example of what it looks like to take DI to its logical conclusion, take a look at Gilad Bracha's Newspeak Programming Language and his writings on the subject:

Constructors Considered Harmful
Lethal Injection
A Ban on Imports (continued)
```

# -*- coding:utf-8 -*-
#!/usr/bin/python3
import os, sys

"""
以下示例显示了pipe()方法的用法。
"""

print ("The child will write text to a pipe and ")
print ("the parent will read the text written by child...")

# file descriptors r, w for reading and writing
r, w = os.pipe() 

processid = os.fork()

if processid:
   # This is the parent process 
   # Closes file descriptor w
   os.close(w)
   r = os.fdopen(r)
   print ("Parent reading")
   str = r.read()
   print ("text =", str   )
   sys.exit(0)
else:
   # This is the child process
   os.close(r)
   w = os.fdopen(w, 'w')
   print ("Child writing")
   w.write("Text written by child...")
   w.close()
   print ("Child closing")
   sys.exit(0)

"""
Python
当运行上述程序时，它会产生以下结果 -

The child will write text to a pipe and
the parent will read the text written by child...
Parent reading
Child writing
Child closing
text = Text written by child...
"""

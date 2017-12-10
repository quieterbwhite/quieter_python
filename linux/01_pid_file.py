ref: https://unix.stackexchange.com/questions/12815/what-are-pid-and-lock-files-for
ref: https://stackoverflow.com/questions/8296170/what-is-a-pid-file-and-what-does-it-contain

What are pid and lock files for?

I often see that programs specify pid and lock files. And I'm not quite sure what they do.

For example, when compiling nginx:

--pid-path=/var/run/nginx.pid \
--lock-path=/var/lock/nginx.lock \
Can somebody shed some light on this one?


pid files are written by some programs to record their process ID while they are starting. This has multiple purposes:

It's a signal to other processes and users of the system that that particular program is running, or at least started successfully.
It allows one to write a script really easy to check if it's running and issue a plain kill command if one wants to end it.
It's a cheap way for a program to see if a previous running instance of it did not exit successfully.
Mere presence of a pid file doesn't guarantee that that particular process id is running, of course, so this method isn't 100% foolproof but "good enough" in a lot of instances. Checking if a particular PID exists in the process table isn't totally portable across UNIX-like operating systems unless you want to depend on the ps utility, which may not be desirable to call in all instances (and I believe some UNIX-like operating systems implement ps differently anyway).

Lock files are used by programs to ensure two (well-behaved) separate instances of a program, which may be running concurrently on one system, don't access something else at the same time. The idea is before the program accesses its resource, it checks for presence of a lock file, and if the lock file exists, either error out or wait for it to go away. When it doesn't exist, the program wanting to "acquire" the resource creates the file, and then other instances that might come across later will wait for this process to be done with it. Of course, this assumes the program "acquiring" the lock does in fact release it and doesn't forget to delete the lock file.

This works because the filesystem under all UNIX-like operating systems enforces serialization, which means only one change to the filesystem actually happens at any given time. Sort of like locks with databases and such.


The pid files contains the process id (a number) of a given program. For example, Apache HTTPD may write it's main process number to a pid file - which is a regular text file, nothing more than that - and later use the information there contained to stop itself. You can also use that information (just do a cat filename.pid) to kill the process yourself, using echo filename.pid | xargs kill

# -*- coding=utf-8 -*-
# Created Time: 2017年09月25日 星期一 16时12分42秒
# File Name: 04_run_env_python.py

"""

#!/usr/bin/env python  的作用?

也可以写成 #!/usr/bin/python 直接指定 python解释器

/usr/bin/python 写死了路径使程序不具备可移植性

而 /usr/bin/env 是指的环境变量

执行命令 /use/bin/env 可以看到

当执行代码的时候，会在环境变量中找到Python解释器来执行程序！

还有:

    加了 #!/usr/bin/env python

    在执行python代码的时候就可以不用  python test.py

    因为程序自己已经知道使用什么解释器来执行自己了

    所以，先赋予执行权限，再 ./test.py 就可以执行了

"""

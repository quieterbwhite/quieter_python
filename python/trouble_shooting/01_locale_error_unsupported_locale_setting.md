#### 解决pip install时unsupported locale setting错误

 发表于 2016-10-22 |  更新于: 2016-10-22

> http://linfuyan.com/locale_error_unsupported_locale_setting/

今天在安装 Shadowsocks 时，使用 `pip install` 命令出现了下面这个错误：

```
# pip install shadowsocks
Traceback (most recent call last):
  File "/usr/bin/pip", line 11, in <module>
    sys.exit(main())
  File "/usr/lib/python2.7/dist-packages/pip/__init__.py", line 215, in main
    locale.setlocale(locale.LC_ALL, '')
  File "/usr/lib/python2.7/locale.py", line 581, in setlocale
    return _setlocale(category, locale)
locale.Error: unsupported locale setting
```

其实是语言配置错误导致的：

```
# locale -a
locale: Cannot set LC_CTYPE to default locale: No such file or directory
C
C.UTF-8
en_AG
en_AG.utf8
en_AU.utf8
en_BW.utf8
en_CA.utf8
en_DK.utf8
en_GB.utf8
en_HK.utf8
en_IE.utf8
...
```

解决方案：

```
# export LC_ALL=C
```

Done!

___

___

> https://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting

The root cause is: your environment variable `LC_ALL` is missing or invalid somehow

**Short answer-**

just run the following command:

```
$ export LC_ALL=C
```

**Long answer-**

Here is my `locale` settings:

```
$ locale
LANG=en_US.UTF-8
LANGUAGE=
LC_CTYPE="C"
LC_NUMERIC="C"
LC_TIME="C"
LC_COLLATE="C"
LC_MONETARY="C"
LC_MESSAGES="C"
LC_PAPER="C"
LC_NAME="C"
LC_ADDRESS="C"
LC_TELEPHONE="C"
LC_MEASUREMENT="C"
LC_IDENTIFICATION="C"
LC_ALL=C
```

*Python2.7*

```
    $ uname -a
    Linux debian 3.16.0-4-amd64 #1 SMP Debian 3.16.7-ckt11-1+deb8u6 (2015-11-09) x86_64 GNU/Linux
    $ python --version
    Python 2.7.9
    $ pip --version
    pip 8.1.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)
    $ unset LC_ALL
    $ pip install virtualenv
    Traceback (most recent call last):
      File "/usr/local/bin/pip", line 11, in <module>
        sys.exit(main())
      File "/usr/local/lib/python2.7/dist-packages/pip/__init__.py", line 215, in main
        locale.setlocale(locale.LC_ALL, '')
      File "/usr/lib/python2.7/locale.py", line 579, in setlocale
        return _setlocale(category, locale)
    locale.Error: unsupported locale setting
    $ export LC_ALL=C
    $ pip install virtualenv
    Requirement already satisfied (use --upgrade to upgrade): virtualenv in /usr/local/lib/python2.7/dist-packages
```
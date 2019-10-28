#### soffice libreoffice doc word pdf 转

##### Error: source file could not be loaded 使用Libreoffice转换文档
```
https://github.com/samvera/hydra-derivatives/issues/116
https://stackoverflow.com/questions/37772250/using-soffice-within-python-command-works-in-terminal-but-not-in-python-subproc
Q:
    Libreoffice returns zero status when it errors:
    awead@pooh T $ soffice --invisible --headless --convert-to doc --outdir /. non-existent-file.txt
    Error: source file could not be loaded
    awead@pooh T $ echo $?

rifuentesm commented on Jan 18, 2017
    Hi, i have the same problem on Ubuntu Server 16.04 when trying to convert files, only the "file could not be loaded". I think its something that is not installed.
    The problem was solved installing the complete libreoffice suite (sudo apt-get install libreoffice) not only the "commons" package (sudo apt-get install libreoffice-common).
    Hope this helps.
```

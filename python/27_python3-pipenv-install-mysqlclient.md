# [Python3 - Pipenv install mysqlclient?](https://stackoverflow.com/questions/50604948/python3-pipenv-install-mysqlclient)
> https://stackoverflow.com/questions/50604948/python3-pipenv-install-mysqlclient


You probably need the mysql client lib for the OS.

```
sudo apt install libmysqlclient-dev
```

Then you should be able to:

```
pipenv install mysqlclient
```

---

if you are on Centos

Try: `yum install mariadb-devel`

this package includes the missing `mysql-config`

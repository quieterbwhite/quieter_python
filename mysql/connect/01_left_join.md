#### 5分钟学会MySql的那些左连接、左外连接、内连接等等

首先，我们新建两个表（员工表，和部门表）

```
DROP DATABASE db0206;
CREATE DATABASE db0206;
USE db0206;

CREATE TABLE `db0206`.`tbl_dept`(  
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `deptName` VARCHAR(30),
  `locAdd` VARCHAR(40),
  PRIMARY KEY (`id`)
) ENGINE=INNODB CHARSET=utf8;

CREATE TABLE `db0206`.`tbl_emp`(  
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20),
  `deptId` INT(11),
  PRIMARY KEY (`id`),
  CONSTRAINT emlyee_dept_fk FOREIGN KEY(deptId) REFERENCES tbl_dept(id)
) ENGINE=INNODB CHARSET=utf8;
/*插入数据*/
INSERT INTO tbl_dept(deptName,locAdd) VALUES('RD',11);
INSERT INTO tbl_dept(deptName,locAdd) VALUES('HR',12);
INSERT INTO tbl_dept(deptName,locAdd) VALUES('MK',13);
INSERT INTO tbl_dept(deptName,locAdd) VALUES('MIS',14);
INSERT INTO tbl_dept(deptName,locAdd) VALUES('FD',15);

INSERT INTO tbl_emp(NAME,deptId) VALUES('z3',1);
INSERT INTO tbl_emp(NAME,deptId) VALUES('z4',1);
INSERT INTO tbl_emp(NAME,deptId) VALUES('z5',1);

INSERT INTO tbl_emp(NAME,deptId) VALUES('w5',2);
INSERT INTO tbl_emp(NAME,deptId) VALUES('w6',2);

INSERT INTO tbl_emp(NAME,deptId) VALUES('s7',3);

INSERT INTO tbl_emp(NAME,deptId) VALUES('s8',4);
```

然后，得到两表是这样的

![img](https://img-blog.csdn.net/20180323201414734?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

开始愉快的学习吧

### **1.内连接（内连接就是两张表中都包含的数据，因为部门表包含了员工表，所以内连接就是上图中绿色部分）**

**SELECT \* FROM tbl_dept a INNER JOIN tbl_emp b ON a.id = b.deptId;**

**![img](https://img-blog.csdn.net/20180323201824380?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)**

**可以看出它把员工表中的所有数据都查询出来了，而且连着部门表中相对应的数据也查询出来了**

### **2.左外连接（左外连接就是查询join左边表中的所有数据，并且把join右边表中对应的数据查询出来）**

**SELECT \* FROM tbl_dept a LEFT JOIN tbl_emp b ON a.id=b.deptId;（会查询上图中橙色部分和绿色部分）**

**![img](https://img-blog.csdn.net/20180323202228943?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)**

从上图中可以看出，由于部门表在join的右边，所以查询会把部门表中所有的数据查询出来。而员工表中没有对应的部门只能显示null了。

**如果我们把员工表放join的左边呢？**

**SELECT \* FROM tbl_emp a LEFT JOIN tbl_dept b ON a.deptId=b.id;（查询绿色部分）**

**![img](https://img-blog.csdn.net/2018032320253652?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)**

这样只能把员工表和与之对应的部门表的数据给查询出来了，多余的部门就没有查出来了。就是这么简单

### 3.右外连接（与左外连接正好相反，它查询的是join右边的部分）

SELECT * FROM tbl_dept a RIGHT JOIN tbl_emp b ON a.id = b.deptId;（**查询绿色部分**）

![img](https://img-blog.csdn.net/20180323203357301?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 4左连接（其实就是在左外连接在后面加了一个where条件，查询只存在于join左边表的内容）

**SELECT \* FROM tbl_dept a LEFT JOIN tbl_emp b ON a.id=b.deptId WHERE b.deptId IS NULL;（图中橙色部分）**

**![img](https://img-blog.csdn.net/20180324161757527?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)**

### **5.右连接（和左连接相反，查询只存在于join右边表的数据）**

**SELECT \* FROM tbl_dept a RIGHT JOIN tbl_emp b ON a.id = b.deptId WHERE a.id IS NULL;（由于部门表包含了所有的员工表，所以查出来的是空）**

**![img](https://img-blog.csdn.net/2018032416202862?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)**

### **6.-- 全连接(查询俩张表的全部内容)**

**SELECT \* FROM tbl_dept a RIGHT JOIN tbl_emp b ON a.id=b.deptId UNION SELECT * FROM tbl_dept a LEFT JOIN tbl_emp b ON a.id=b.deptId;（其实就是一个左外连接加一个右外连接，所以把图中橙色部分和绿色部分都查出来了）**

**![img](https://img-blog.csdn.net/20180324162256540?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)**

### **7.-- （两张表中都没有同时出现的数据集）**

**SELECT \* FROM tbl_dept a RIGHT JOIN tbl_emp b ON a.id=b.deptId WHERE a.id IS NULL UNIONSELECT * FROM tbl_dept a LEFT JOIN tbl_emp b ON a.id=b.deptId WHERE b.deptId IS NULL;（也就是图中橙色部分）**

**![img](https://img-blog.csdn.net/2018032416250285?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI5NTQzODA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)**

**完整代码如下**

```mysql
DROP DATABASE db0206;
CREATE DATABASE db0206;
USE db0206;

CREATE TABLE `db0206`.`tbl_dept`(  
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `deptName` VARCHAR(30),
  `locAdd` VARCHAR(40),
  PRIMARY KEY (`id`)
) ENGINE=INNODB CHARSET=utf8;

CREATE TABLE `db0206`.`tbl_emp`(  
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(20),
  `deptId` INT(11),
  PRIMARY KEY (`id`),
  CONSTRAINT emlyee_dept_fk FOREIGN KEY(deptId) REFERENCES tbl_dept(id)
) ENGINE=INNODB CHARSET=utf8;
/*插入数据*/
INSERT INTO tbl_dept(deptName,locAdd) VALUES('RD',11);
INSERT INTO tbl_dept(deptName,locAdd) VALUES('HR',12);
INSERT INTO tbl_dept(deptName,locAdd) VALUES('MK',13);
INSERT INTO tbl_dept(deptName,locAdd) VALUES('MIS',14);
INSERT INTO tbl_dept(deptName,locAdd) VALUES('FD',15);

INSERT INTO tbl_emp(NAME,deptId) VALUES('z3',1);
INSERT INTO tbl_emp(NAME,deptId) VALUES('z4',1);
INSERT INTO tbl_emp(NAME,deptId) VALUES('z5',1);

INSERT INTO tbl_emp(NAME,deptId) VALUES('w5',2);
INSERT INTO tbl_emp(NAME,deptId) VALUES('w6',2);

INSERT INTO tbl_emp(NAME,deptId) VALUES('s7',3);

INSERT INTO tbl_emp(NAME,deptId) VALUES('s8',4);


-- 内连接(查询两个表都存在的内容)
SELECT * FROM tbl_dept a INNER JOIN tbl_emp b ON a.id = b.deptId;


-- 左外连接(查询join左边表的全部内容)
SELECT * FROM tbl_dept a LEFT JOIN tbl_emp b ON a.id=b.deptId;
SELECT * FROM tbl_dept LEFT JOIN tbl_emp ON tbl_dept.id = tbl_emp.deptId;

SELECT * FROM tbl_emp a LEFT JOIN tbl_dept b ON a.deptId=b.id;
SELECT * FROM tbl_emp LEFT JOIN tbl_dept ON tbl_emp.deptId=tbl_dept.id;


-- 右外连接（查询join右边表的全部内容）
SELECT * FROM tbl_dept a RIGHT JOIN tbl_emp b ON a.id = b.deptId;

SELECT * FROM tbl_emp a RIGHT JOIN tbl_dept b ON a.deptId = b.id;


-- 左连接（查询只存在于join左边表的内容）
SELECT * FROM tbl_dept a LEFT JOIN tbl_emp b ON a.id=b.deptId WHERE b.deptId IS NULL;

SELECT * FROM tbl_emp a LEFT JOIN tbl_dept b ON a.deptId = b.id WHERE b.id IS NULL;

-- 右连接（查询只存在于join右边表的内容）
SELECT * FROM tbl_dept a RIGHT JOIN tbl_emp b ON a.id = b.deptId WHERE a.id IS NULL;

SELECT * FROM tbl_emp a RIGHT JOIN tbl_dept b ON a.deptId = b.id WHERE a.deptId IS NULL;


-- 全连接(查询俩张表的全部内容)
SELECT * FROM tbl_dept a RIGHT JOIN tbl_emp b ON a.id=b.deptId 
UNION 
SELECT * FROM tbl_dept a LEFT JOIN tbl_emp b ON a.id=b.deptId;

-- 两张表中都没有出现的数据集
SELECT * FROM tbl_dept a RIGHT JOIN tbl_emp b ON a.id=b.deptId WHERE a.id IS NULL 
UNION
SELECT * FROM tbl_dept a LEFT JOIN tbl_emp b ON a.id=b.deptId WHERE b.deptId IS NULL;
```
# [MySQL Split 函数](https://www.cnblogs.com/qiaoyihang/p/6270165.html)

本文地址：http://www.cnblogs.com/qiaoyihang/p/6270165.html

mysql 本身并没有 split 函数，但是，我们实现累死功能的自定义函数是非常简单的

**创建函数的语法**

用户自定义函数是拓展mysql函数的一种方式，它用起来和mysql本身自带的函数没有什么区别

创建一个自定义函数的语法：

```
CREATE [AGGREGATE] FUNCTION function_name
RETURNS {STRING|INTEGER|REAL|DECIMAL}
```

**split  函数**

```
CREATE FUNCTION SPLIT_STR(
  x VARCHAR(255),
  delim VARCHAR(12),
  pos INT
)
RETURNS VARCHAR(255)
RETURN REPLACE(SUBSTRING(SUBSTRING_INDEX(x, delim, pos),
       LENGTH(SUBSTRING_INDEX(x, delim, pos -1)) + 1),
       delim, '');
```

**用法：**

```
SELECT SPLIT_STR(string, delimiter, position)
```

**例子：**

```
SELECT SPLIT_STR('a|bb|ccc|dd', '|', 3) as third;

+-------+
| third |
+-------+
| ccc   |
+-------+
```
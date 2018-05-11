<%--
  Created by IntelliJ IDEA.
  User: bwhite
  Date: 18-5-11
  Time: 下午4:01
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Login</title>
</head>
<body>
<h1> 欢饮登录 </h1>
<form action="/loginUser" method="post">
    <input type="text" name="username"> <br>
    <input type="text" name="password"> <br>
    <input type="submit" name="提交"> <br>
</form>
</body>
</html>

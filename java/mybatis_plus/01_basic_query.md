#### Mybatis-Plus 查询语句例子

```java
public static void testCrud() {
        // 自己手写的方式
        //System.out.println(userDao.selectByPrimaryId(1));

        // 自动生成的代码
        // 增
        User user01 = new User();
        user01.setName("测试添加");
        userDao.insert(user01);

        //删
        Integer influenceRows = userDao.deleteById(2);
        System.out.println("影响行数："+influenceRows);

        //修改
        User user02=new User();
        user02.setId(3);
        user02.setName("update测试");
        System.out.println("update影响行数"+userDao.updateById(user02));

        // 查
        User user03 = userDao.selectById(3);
        System.out.println(user03);

        //分页查询
        Wrapper<User> entity = new EntityWrapper<User>();
        entity.like("name", "%测试%");
        entity.between("id", 1, 3);
        List<User> lstUser = userDao.selectPage(new Page<User>(1,10),entity);
        for(User user:lstUser) {
            System.out.println(user);
        }
  
        User userObj = userService.selectOne(
                      new EntityWrapper<User>()
                      .eq("username", user.getUsername())
              );
    }
```


## scala中的continue和break

[张  张欢19933](https://my.oschina.net/u/2000675) 发布于 2018/04/27 14:57

(1)break例子

```scala
breakable(
    for(i<-0 until 10) {
      println(i)
      if(i==5){
        break()
      }
    }
  )
 // 0,1,2,3,4,5
```

(2)continue例子

```scala
for(i<-0 until 10){
      breakable{
      if(i==3||i==6) {
        break
      }
      println(i)
      }
    }
    //0,1,2,3,5,7,8,9
```

需要导入的包：

```
import scala.util.control.Breaks._
```
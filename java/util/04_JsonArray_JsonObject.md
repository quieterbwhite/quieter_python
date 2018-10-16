#### JSON学习（四）：JsonArray和JsonObject遍历方法

2017年04月10日 16:25:53  changhenshui1990

个人分类： [JAVA基础-JSON和XML](https://blog.csdn.net/changhenshui1990/article/category/6947334)

版权声明：本文为博主原创文章，未经博主允许不得转载。	https://blog.csdn.net/changhenshui1990/article/details/69950663

一：遍历JsonArray

```java
 // 一个未转化的字符串
String str = "[{name:'a',value:'aa'},{name:'b',value:'bb'},{name:'c',value:'cc'},{name:'d',value:'dd'}]" ; 
 // 首先把字符串转成 JSONArray  对象
JSONArray json = JSONArray.fromObject(str );
if(json.size()>0){
  for(int i=0;i<json.size();i++){
 // 遍历 jsonarray 数组，把每一个对象转成 json 对象
JSONObject job = json.getJSONObject(i); 
// 得到 每个对象中的属性值
System.out.println(job.get("name")+"=") ;  
  }
}
```

一：遍历JsonObject

```java
JSONObject jsonObject = new JSONObject(s);
//然后用Iterator迭代器遍历取值，建议用反射机制解析到封装好的对象中
JSONObject jsonObject = new JSONObject(jsonString);
        Iterator iterator = jsonObject.keys();
while(iterator.hasNext()){
            key = (String) iterator.next();
        value = jsonObject.getString(key);
}
```






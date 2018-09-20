#### angularjs设置请求头信息

>   https://blog.csdn.net/qq_28259083/article/details/77725263

1.  ​

```js
module.config(['$httpProvider',function($httpProvider){
    $httpProvider.interceptors.push('authInterceptor');
}])
.factory('authInterceptor', function($rootScope,  $cookies){
    return {
        request: function(config){
            config.headers = config.headers || {};
            if(new RegExp("isearch").test(config.url) && "POST" == config.method){
                if($cookies.get('token')){
                    config.headers['token'] = $cookies.get('token');
                }
            }
            return config;
        },
        responseError: function(response){
            // ...
        }
    };
})
```

1.  在http服务的在服务端发送请求时，也就是调用http()方法时，在config对象中设置请求头信息：示例如下, 这种方法的好处就是针对不同路径的请求，可以个性化配置请求头部，缺点就是，不同路径请求都需要单独配置。

```js
$http.post('/somePath' , someData , {
        headers : {'token' : getCookie('token')}
    }).success(function(data, status, headers, config) {
        //...
    }).error(function(data, status, headers, config ) {
        //...
    });
```

**设置某个get请求禁用浏览器缓存**

```js
$http.get(settingUrl,{
            headers : {'Expires':0,'Cache-Control':'no-cache','Pragma':'no-cache'}
        }).success(function(results){

        });
```

1.  第二种设置请求头信息的方式就是在$httpProvider.defaults.headers属性上直接配置。事例如下：

```js
myModule
.config(function($httpProvider) {
    $httpProvider.defaults.headers.post= { 'token' : getCookie('token') }
})
```

$httpProvider.defaults.headers有不同的属性，如common、get、post、put等。因此可以在不同的http请求上面添加不同的头信息，common是指所有的请求方式。

这种方式添加请求头信息的优势就是可以给不同请求方式添加相同的请求头信息，缺点就是不能够为某些请求path添加个性化头信息。

1.  第三种设置请求头信息的地方是$httpProvider.interceptors。也就是为请求或相应注册一个拦截器。这种方法就是上面用到的。 首先定义一个服务：

    ```js
    myModule.factory('authInterceptor', function($rootScope,  $cookies){
        return {
            request: function(config){
                config.headers = config.headers || {};
                if($cookies.get('token')){
                    config.headers['token'] = $cookies.get('token');
                }
                return config;
            },
            responseError: function(response){
                // ...
            }
        };
    })
    ```

    上面的config貌似就是请求头，可以根据config，为特定的请求方式添加请求头信息。 
    然后把上面定义的服务注册到$httpProvider.interceptors中。

    ```js
    .config(function($httpProvider){
        $httpProvider.interceptors.push('authInterceptor');
    })
    ```

    这样，对于每次请求，不论是get还是post、put。我们都会在请求头信息中加入authorization属性。这种方式在处理验权、授权方面很有用的。

    说明：文中getCookie(‘token’)为自定义函数

    ```js
    function getCookie(name) {
        if (name != null) {
            var value = new RegExp("(?:^|; )" + encodeURIComponent(String(name)) + "=([^;]*)").exec(document.cookie);
            return value ? decodeURIComponent(value[1]) : null;
        }
    }
    ```

    ​
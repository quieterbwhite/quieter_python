#### [node.js – axios：https请求代理](https://codeday.me/bug/20190130/586939.html)

```
const url = "https://walmart.com/ip/50676589"
var config = { proxy: { host: proxy.ip, port: proxy.port } }

axios.get(url, config)
.then(result => {})
.catch(error => {console.log(error)})
```



试试这个.这对我有用.

第一

npm install axios-https-proxy-fix

然后

```
import axios from 'axios-https-proxy-fix'; 

const proxy = {
  host: 'some_ip',
  port: some_port_number,
  auth: {
    username: 'some_login',
    password: 'some_pass'
  }
};

async someMethod() {
  const result = await axios.get('some_https_link', {proxy});
}
```
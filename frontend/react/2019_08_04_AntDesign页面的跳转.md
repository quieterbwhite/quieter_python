#### Ant Design 页面的跳转

2018年12月05日 11:56:23 [LoveEate](https://me.csdn.net/LoveEate) 阅读数 3186

import {routerRedux} from 'dva/router';

在页面时跳转使用

dispatch(routerRedux.push('/'));

在model里面跳转

yield put(routerRedux.push('/'));

---

routerRedux方式

```javascript
import { routerRedux } from 'dva/router';

goOrder (record){//页面跳转+参数
    this.props.dispatch(routerRedux.push({ 
      pathname: '/giveData/queryOrder',
      params: record.userId
    }))
  }

<a className={styles.oprLink} onClick={()=>this.goOrder(record)}>查订单</a>

// 使用this.props.location.params接收值
// https://blog.csdn.net/qq_25252769/article/details/79958487 
```

Link方式

```javascript
import { Link } from 'react-router-dom';
或者
import { Link } from 'dva/router';

<Link to={{pathname:'/user',query:id}}>添加用户</Link>

// 使用v2，v3this.props.location.query或者v4的this.props.location.search接收值
```


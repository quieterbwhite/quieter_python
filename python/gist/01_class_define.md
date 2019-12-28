# 定义类
> https://github.com/QianmiOpen/dubbo-client-py  
```python
class ApplicationConfig(object):
    # 应用名称
    name = 'default'
    # 模块版本
    version = '1.0.0'
    # 应用负责人
    owner = ''
    # 组织名(BU或部门)
    organization = ''
    # 分层
    architecture = 'web'
    # 环境，如：dev/test/run
    environment = 'run'

    def __init__(self, name, **kwargs):
        self.name = name
        object_property = dir(ApplicationConfig)
        for key, value in kwargs.items():
            if key in object_property:
                setattr(self, key, value)

    def __str__(self):
        return 'ApplicationConfig is {0}'.format(",".join(k + ':' + v for k, v in vars(self).iteritems()))
```

又一个
> http://beginman.cn/python/2017/03/09/python-a-controlled-configuration/  
```python
import copy
import uuid


class Simple(object):
    DEFAULT_CONFIG = {
        'host': 'localhost',
        'client_id': None,
        'api_version': '1.0.0'
    }

    def __init__(self, **configs):
        self.config = copy.copy(self.DEFAULT_CONFIG)
        for key in self.config:
            if key in configs:
                self.config[key] = configs.pop(key)
        
        # Only check for extra config keys in top-level class
        assert not configs, 'Unrecognized configs: %s' % configs

        if self.config['client_id'] is None:
            self.config['client_id'] = str(uuid.uuid4())

if __name__ == '__main__':
    sim = Simple()
    print(sim.config)
    
    sim = Simple(host='192.168.1.129', client_id='demo')
    print(sim.config)

    # sim = Simple(api_version="1.1.1", other="other value")
    # AssertionError: Unrecognized configs: {'other': 'other value'} 
```

#-*- encoding=utf-8 -*-

def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton():  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton 



'''
if __name__ == '__main__':

@singleton
class test(object):
    def __init__(self):
        self.x = 1


a = test()
b = test()

a.x = 1
b.x = 2

print a.x
print b.x

'''


#### Django之数据库并发处理

##### https://blog.csdn.net/m0_37714245/article/details/82027543

##### 核心代码
```python
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from app01.models import GoodsInfo

class Goods(GenericAPIView):
    """ 购买商品 """
    def post(self, request):
        # 获取请求头中查询字符串数据
        goods_id = request.GET.get('goods_id')
        count = int(request.GET.get('count'))

        while True:
            # 查询商品对象
            goods = GoodsInfo.objects.filter(id=goods_id).first()
            # 获取原始库存
            origin_stock = goods.stock

            # 判断商品库存是否充足
            if origin_stock < count:
                return HttpResponse(content="商品库存不足", status=400)

            # 演示并发请求
            import time
            time.sleep(5)

            # 减少商品的库存数量，保存到数据库
            # goods.stock = origin_stock - count
            # goods.save()
            """ 使用乐观锁进行处理，一步完成数据库的查询和更新 """
            # update返回受影响的行数
            result = GoodsInfo.objects.filter(id=goods.id, stock=origin_stock).update(stock=origin_stock - count)
            if result == 0:
                # 表示更新失败，有人抢先购买了商品，重新获取库存信息，判断库存
                continue

            # 表示购买成功，退出 while 循环
            break

        return HttpResponse(content="操作成功", status=200)
```






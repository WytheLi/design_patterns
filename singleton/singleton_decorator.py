def singleton(cls):
    """ 单例装饰器 """
    _instance = dict()  # 为什么这里定义 _instance=None在嵌套函数中获取不到该变量

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return _singleton


@singleton
class A(object):
    a = 1
    def __init__(self, x=0):
        self.x = x

a1 = A(1)
a2 = A(2)
print(a1.x, a2.x)

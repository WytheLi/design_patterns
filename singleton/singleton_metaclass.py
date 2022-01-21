"""
metaclass - 元类type
1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法。
示例如下：
"""
import threading


class Foo(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

obj = Foo() # 执行type的 __call__ 方法，调用 type 的 __new__方法，用于创建对象，然后调用 type 的 __init__方法，用于对对象初始化。

obj()    # 执行Foo的 __call__ 方法


############################### 元类的使用 ###############################
class SingletonType(type):

    def __init__(self, *args, **kwargs):
        super(SingletonType, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)
        return obj


class Foo(metaclass=SingletonType):

    def __init__(self, uid):
        self.uid = uid

    def __new__(cls, *args, **kwargs):
        return super(Foo, cls).__new__(cls)

obj1 = Foo(1)
print(obj1)


############################### 单例模式 - 元类实现 ###############################
class SingletonType(type):
    _thread_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._thread_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingletonType):
    def __init__(self, uid=None):
        self.uid = uid


obj2 = Foo(2)
obj3 = Foo(3)
print(obj2, obj3)

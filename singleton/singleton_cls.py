import threading
import time


class Singleton(object):
    """ 类开关值 """
    _thread_lock = threading.Lock()

    def __init__(self, uid=None):
        time.sleep(0.1)
        self.uid = uid

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):     # 防止已经是单例了，无需加锁徒增开销
            with cls._thread_lock:     # 此处不加锁无法在多线程中实现单例
                if not hasattr(Singleton, "_instance"):
                    cls._instance = cls(*args, **kwargs)
        return cls._instance


def task(uid):
    # 单例实例化必须通过 obj = Singleton.instance()，不然得不到单例
    obj = Singleton.instance(uid)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=[i,])
    t.start()

import threading


class Singleton(object):
    _thread_lock = threading.Lock()

    def __init__(self, uid=None):
        self.uid = uid

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with cls._thread_lock:
                if not hasattr(Singleton, "_instance"):
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


def task(uid):
    obj = Singleton(uid)
    print(obj)


for i in range(10):
    t = threading.Thread(target=task, args=(i,))
    t.start()

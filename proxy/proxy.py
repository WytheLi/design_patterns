from abc import ABC, abstractmethod


class Subject(ABC):
    """ 抽象类 """
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """ 实现类 """
    def request(self) -> None:
        print("RealSubject: 处理请求")


class Proxy(Subject):
    """ 代理类 """
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: 检查访问权限")
        return True

    def log_access(self) -> None:
        print("Proxy: 记录请求时间")


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()

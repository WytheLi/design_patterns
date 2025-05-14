from proxy.proxy import Subject, RealSubject


class ProtectedProxy(Subject):
    """ 权限控制代理 """
    def __init__(self, real_subject: RealSubject, user_role: str) -> None:
        self._real_subject = real_subject
        self.user_role = user_role

    def request(self) -> None:
        if self.user_role == "admin":
            print("ProtectedProxy: 管理员权限验证通过")
            self._real_subject.request()
        else:
            raise Exception("ProtectedProxy: 权限不足")


if __name__ == "__main__":
    try:
        proxy = ProtectedProxy(RealSubject(), "user")
        proxy.request()
    except Exception as e:
        print(str(e))

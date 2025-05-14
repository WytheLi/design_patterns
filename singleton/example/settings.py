from singleton.singleton_metaclass import SingletonType


class Settings(metaclass=SingletonType):
    """
    应用全局配置类，确保全局配置唯一，避免重复加载文件或环境变量。
    """
    def __init__(self):
        self.config = {}
        self._load_config()

    def _load_config(self):
        # 从文件或环境变量加载配置
        self.config["DATABASE_URI"] = "mysql://user:pass@localhost/db"

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value


if __name__ == "__main__":
    s1 = Settings()
    s2 = Settings()
    print(s1.get("DATABASE_URI"))

    s1.set("DATABASE_URI", "mysql://user:pass@localhost/db1")
    print(s2.get("DATABASE_URI"))

from abc import abstractmethod, ABC


class DatabaseQuery(ABC):
    @abstractmethod
    def execute_query(self, sql: str) -> dict:
        pass


class RealDatabaseQuery(DatabaseQuery):
    """
    真实数据库操作，这里实现真实的db查库
    """
    def execute_query(self, sql: str) -> dict:
        print(f"执行数据库查询: {sql}")
        # 模拟数据库返回
        return {"data": [1, 2, 3], "sql": sql}


class CachedDatabaseProxy(DatabaseQuery):
    """ 数据库查询缓存代理 """
    def __init__(self) -> None:
        self._real_db = RealDatabaseQuery()
        self._cache = {}

    def execute_query(self, sql: str) -> dict:
        if sql in self._cache:
            print(f"缓存命中: {sql}")
            return self._cache[sql]

        result = self._real_db.execute_query(sql)
        self._cache[sql] = result
        print("将结果存入缓存")
        return result


if __name__ == "__main__":
    db_proxy = CachedDatabaseProxy()
    print(db_proxy.execute_query("SELECT * FROM users"))  # db查库
    print(db_proxy.execute_query("SELECT * FROM users"))  # 从缓存获取
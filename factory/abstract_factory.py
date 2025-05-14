from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    """ 抽象数据库连接类 """
    @abstractmethod
    def connect(self) -> str:
        pass


class DatabaseCursor(ABC):
    """ 抽象数据库CURD类"""
    @abstractmethod
    def execute(self, query: str) -> str:
        pass


class MySQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "MySQL 连接已建立"


class MySQLCursor(DatabaseCursor):
    def execute(self, query: str) -> str:
        return f"MySQL 执行查询: {query}"


class PostgreSQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "PostgreSQL 连接已建立"


class PostgreSQLCursor(DatabaseCursor):
    def execute(self, query: str) -> str:
        return f"PostgreSQL 执行查询: {query}"


class DatabaseFactory(ABC):
    """ 抽象工厂类 """
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass

    @abstractmethod
    def create_cursor(self) -> DatabaseCursor:
        pass


class MySQLFactory(DatabaseFactory):
    """ Mysql操作工厂 """
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()

    def create_cursor(self) -> DatabaseCursor:
        return MySQLCursor()


class PostgreSQLFactory(DatabaseFactory):
    """ PG操作工厂类 """
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

    def create_cursor(self) -> DatabaseCursor:
        return PostgreSQLCursor()


def database_client(factory: DatabaseFactory) -> None:
    """ 客户端调用 """
    connection = factory.create_connection()
    cursor = factory.create_cursor()
    print(connection.connect())
    print(cursor.execute("SELECT * FROM users"))


if __name__ == "__main__":
    database_client(MySQLFactory())
    # 输出:
    # MySQL 连接已建立
    # MySQL 执行查询: SELECT * FROM users

    database_client(PostgreSQLFactory())
    # 输出:
    # PostgreSQL 连接已建立
    # PostgreSQL 执行查询: SELECT * FROM users
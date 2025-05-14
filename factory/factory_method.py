from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """ 抽象产品类 """
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass


class AlipayProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"支付宝支付 {amount} 元成功"

class WechatPayProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"微信支付 {amount} 元成功"


class PaymentFactory(ABC):
    """ 抽象工厂类 """
    @abstractmethod
    def create_processor(self) -> PaymentProcessor:
        pass


class AlipayFactory(PaymentFactory):
    def create_processor(self) -> PaymentProcessor:
        return AlipayProcessor()

class WechatPayFactory(PaymentFactory):
    def create_processor(self) -> PaymentProcessor:
        return WechatPayProcessor()


def client_code(factory: PaymentFactory) -> None:
    processor = factory.create_processor()
    print(processor.process_payment(100.0))


if __name__ == "__main__":
    client_code(AlipayFactory())  # 输出: 支付宝支付 100.0 元成功
    client_code(WechatPayFactory())  # 输出: 微信支付 100.0 元成功

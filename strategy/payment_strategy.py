from abc import ABC, abstractmethod

######################################################################################################################
# 支付场景处理。支付网关切换，快速接入/切换不同支付渠道（支付宝/微信/银联）
######################################################################################################################


class PaymentStrategy(ABC):
    """ 策略接口 """
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class AlipayStrategy(PaymentStrategy):
    """ 业务实现类 """
    def pay(self, amount: float) -> None:
        print(f"支付宝支付：{amount:.2f}元")


class WechatPayStrategy(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"微信支付：{amount:.2f}元")


class CreditCardStrategy(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"信用卡支付：{amount:.2f}元")


class PaymentProcessor:
    """ 上下文类 """
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount: float):
        self._strategy.pay(amount)


if __name__ == "__main__":
    # 创建支付处理器并设置默认策略
    processor = PaymentProcessor(AlipayStrategy())

    # 执行支付
    processor.execute_payment(100.50)  # 支付宝支付：100.50元

    # 动态切换策略
    processor.set_strategy(CreditCardStrategy())
    processor.execute_payment(200.0)  # 信用卡支付：200.00元

from abc import ABC, abstractmethod
from typing import List


class DiscountStrategy(ABC):
    """ 策略接口 """
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass


class NoDiscountStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price


class MemberDiscountStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.9  # 9折


class BlackFridayDiscountStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price * 0.7  # 7折


class OrderProcessor:
    """ 订单的聚合处理类 """
    def __init__(self, strategy: DiscountStrategy = NoDiscountStrategy()):
        self._strategy = strategy

    def set_discount_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def calculate_total(self, prices: List[float]) -> float:
        return sum(self._strategy.apply_discount(price) for price in prices)


if __name__ == "__main__":
    order = OrderProcessor()
    prices = [100.0, 200.0, 300.0]

    print("默认价格:", order.calculate_total(prices))  # 600.0

    order.set_discount_strategy(MemberDiscountStrategy())
    print("会员折扣:", order.calculate_total(prices))  # 540.0

    order.set_discount_strategy(BlackFridayDiscountStrategy())
    print("黑五折扣:", order.calculate_total(prices))  # 420.0
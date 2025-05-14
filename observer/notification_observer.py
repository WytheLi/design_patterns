from abc import ABC, abstractmethod
import datetime


# 抽象主题接口
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self, event_data):
        pass


# 抽象观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, event_data):
        pass


# 具体主题：订单管理系统
class OrderSubject(Subject):
    def __init__(self, order_id):
        self._observers = []
        self.order_id = order_id
        self._state = "CREATED"  # 初始状态

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, event_data):
        for observer in self._observers:
            observer.update(event_data)

    def update_state(self, new_state):
        old_state = self._state
        self._state = new_state

        # 构造事件数据
        event_data = {
            "order_id": self.order_id,
            "old_state": old_state,
            "new_state": new_state,
            "timestamp": datetime.datetime.now().isoformat(),
            "metadata": {"source": "OrderSystem"}
        }

        self.notify_observers(event_data)


# 具体观察者：库存管理系统
class InventoryObserver(Observer):
    def update(self, event_data):
        if event_data["new_state"] == "SHIPPED":
            print(f"[Inventory] Order {event_data['order_id']} shipped. "
                  f"Updating stock levels...")

        elif event_data["new_state"] == "CANCELLED":
            print(f"[Inventory] Order {event_data['order_id']} cancelled. "
                  f"Restoring stock...")


# 具体观察者：物流系统
class LogisticsObserver(Observer):
    def update(self, event_data):
        if event_data["new_state"] == "SHIPPED":
            print(f"[Logistics] Scheduling delivery for "
                  f"order {event_data['order_id']}...")


# 具体观察者：客户通知服务
class CustomerNotificationObserver(Observer):
    def update(self, event_data):
        state_map = {
            "SHIPPED": "has been shipped",
            "DELIVERED": "has been delivered",
            "CANCELLED": "was cancelled"
        }

        if event_data["new_state"] in state_map:
            print(f"[Notification] SMS/Email sent: Order {event_data['order_id']} {state_map[event_data['new_state']]}")


if __name__ == "__main__":
    # 创建订单主题
    order = OrderSubject("ORDER_20230715_001")

    # 创建观察者实例
    inventory = InventoryObserver()
    logistics = LogisticsObserver()
    notifications = CustomerNotificationObserver()

    # 注册观察者
    order.register_observer(inventory)
    order.register_observer(logistics)
    order.register_observer(notifications)

    # 模拟订单状态变化
    order.update_state("PROCESSING")
    order.update_state("SHIPPED")  # 触发通知
    print("\n--- Order cancelled scenario ---")
    order.update_state("CANCELLED")  # 触发取消相关逻辑
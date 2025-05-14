from abc import ABC, abstractmethod
import logging

# 配置基础日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OrderProcessingTemplate(ABC):
    """
    订单处理模板类（抽象基类）
    定义订单处理的标准流程
    """

    def process_order(self):
        """模板方法：定义订单处理流程的骨架"""
        self.validate_order()
        self.execute_payment()
        self.update_inventory()
        self.notify_shipment()
        self.finalize_order()

    def validate_order(self):
        """验证订单（具体方法，已有默认实现）"""
        logger.info("验证订单基本信息...")
        # 检查订单号、用户信息等
        # 可以添加具体的验证逻辑
        logger.info("订单验证通过")

    @abstractmethod
    def execute_payment(self):
        """执行支付（抽象方法，必须由子类实现）"""
        pass

    def update_inventory(self):
        """更新库存（具体方法）"""
        logger.info("扣除商品库存...")
        # 实际项目中这里会连接库存管理系统
        logger.info("库存更新完成")

    def notify_shipment(self):
        """通知发货（具体方法）"""
        logger.info("发送发货邮件通知...")
        # 默认使用邮件通知
        # 实际可能集成邮件服务

    def finalize_order(self):
        """订单收尾处理（钩子方法）"""
        # 可选步骤，子类可以视情况覆盖
        logger.info("清理临时数据，关闭订单会话")


class CreditCardPaymentProcessor(OrderProcessingTemplate):
    """信用卡支付处理实现"""

    def execute_payment(self):
        logger.info("处理信用卡支付...")
        # 调用信用卡支付网关
        # 包含PCI DSS合规处理
        logger.info("信用卡支付成功，交易ID: CC-202309251234")


class AlipayPaymentProcessor(OrderProcessingTemplate):
    """支付宝支付处理实现"""

    def execute_payment(self):
        logger.info("处理支付宝支付...")
        # 调用支付宝SDK
        # 处理人民币结算
        logger.info("支付宝支付成功，交易ID: ALI-202309251235")

    def notify_shipment(self):
        """覆盖默认通知方式"""
        logger.info("发送支付宝小程序物流通知...")
        # 使用支付宝提供的通知接口


class InternationalPayPalProcessor(OrderProcessingTemplate):
    """国际PayPal支付处理（带货币转换）"""

    def execute_payment(self):
        logger.info("处理PayPal国际支付...")
        # 处理货币转换
        # 遵守国际贸易条款
        logger.info("PayPal支付成功，交易ID: PP-202309251236")

    def validate_order(self):
        """增加国际订单验证"""
        super().validate_order()
        logger.info("验证海关申报信息...")
        # 添加国际贸易特有的验证逻辑


if __name__ == "__main__":
    print("处理国内信用卡订单:")
    credit_card_processor = CreditCardPaymentProcessor()
    credit_card_processor.process_order()

    print("\n处理支付宝订单:")
    alipay_processor = AlipayPaymentProcessor()
    alipay_processor.process_order()

    print("\n处理国际PayPal订单:")
    paypal_processor = InternationalPayPalProcessor()
    paypal_processor.process_order()
from abc import ABC, abstractmethod
import logging
from typing import Optional, Union

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ExpenseReport:
    """报销申请数据类"""

    def __init__(self, employee_id: str, amount: float, description: str):
        self.employee_id = employee_id
        self.amount = amount
        self.description = description
        self.approved = False
        self.approved_by = []


class ApprovalHandler(ABC):
    """审批处理者抽象基类"""

    def __init__(self):
        self._next_handler: Optional[ApprovalHandler] = None

    def set_next(self, handler: 'ApprovalHandler') -> 'ApprovalHandler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: ExpenseReport) -> Optional[str]:
        pass

    def _pass_to_next(self, request: ExpenseReport) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        logger.warning("Reached end of approval chain without resolution")
        return None


class ManagerHandler(ApprovalHandler):
    """部门经理审批处理者"""
    APPROVAL_LIMIT = 1000.00

    def handle(self, request: ExpenseReport) -> Optional[str]:
        if request.amount <= self.APPROVAL_LIMIT:
            request.approved = True
            request.approved_by.append("Manager")
            logger.info(f"Manager approved {request.amount} expense")
            return f"Approved by Manager (Limit: {self.APPROVAL_LIMIT})"
        logger.debug(f"Manager passing request to next handler")
        return self._pass_to_next(request)


class DirectorHandler(ApprovalHandler):
    """总监审批处理者"""
    APPROVAL_LIMIT = 5000.00

    def handle(self, request: ExpenseReport) -> Optional[str]:
        if request.amount <= self.APPROVAL_LIMIT:
            request.approved = True
            request.approved_by.append("Director")
            logger.info(f"Director approved {request.amount} expense")
            return f"Approved by Director (Limit: {self.APPROVAL_LIMIT})"
        logger.debug(f"Director passing request to next handler")
        return self._pass_to_next(request)


class CEOHandler(ApprovalHandler):
    """CEO审批处理者（最终处理者）"""

    def handle(self, request: ExpenseReport) -> Optional[str]:
        request.approved = True
        request.approved_by.append("CEO")
        logger.info(f"CEO approved {request.amount} expense")
        return "Approved by CEO (Unlimited authority)"


class AuditSystem:
    """审计系统（可选的后置处理）"""

    @staticmethod
    def log_approval(request: ExpenseReport):
        logger.info(f"Audit log: Request {request.amount} approved by {request.approved_by}")


def setup_approval_chain() -> ApprovalHandler:
    """构建并返回配置好的责任链"""
    manager = ManagerHandler()
    director = DirectorHandler()
    ceo = CEOHandler()

    manager.set_next(director).set_next(ceo)
    return manager


def client_code(handler: ApprovalHandler, request: ExpenseReport) -> None:
    """客户端调用代码"""
    result = handler.handle(request)
    if result:
        print(f"审批结果: {result}")
        AuditSystem.log_approval(request)
    else:
        print("审批请求未被处理")


if __name__ == "__main__":
    # 初始化责任链
    approval_chain = setup_approval_chain()

    # 测试不同金额的报销申请
    test_cases = [
        ExpenseReport("EMP001", 800.00, "Office supplies"),
        ExpenseReport("EMP002", 3500.00, "Conference expenses"),
        ExpenseReport("EMP003", 15000.00, "Team building event"),
    ]

    for case in test_cases:
        print(f"\n处理报销申请：{case.description} 金额：{case.amount}")
        client_code(approval_chain, case)
        print(f"审批状态：{'通过' if case.approved else '拒绝'}")

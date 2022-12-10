from .prototype import Prototype
from copy import deepcopy


class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "Knight"


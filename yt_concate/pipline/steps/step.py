# 1.建立所有步驟都要用的class
from abc import ABC
from abc import abstractmethod


# 建立抽象類別(不用建立實例）,至少要有 >=1 的抽象method（@abstractmethod）
class Step(ABC):
    def __init__(self):
        pass

    # 建立抽象（method）,繼承時一定要寫出
    @abstractmethod
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    pass

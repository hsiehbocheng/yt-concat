from abc import abstractmethod, ABC

class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, inputs, data, utils):
        pass

class StepException(Exception):
    pass

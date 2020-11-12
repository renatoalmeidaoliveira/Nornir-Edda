from abc import ABC, abstractmethod

class ModelSyntaxError(Exception):
    pass


class Model(ABC):

    @abstractmethod
    def getModelData(self):
        pass

    @abstractmethod
    def getModel(self):
        pass

    @abstractmethod
    def _lintModel(self):
        pass

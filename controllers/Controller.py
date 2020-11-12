from abc import ABC, abstractmethod
from models.Model import Model
from nornir.core.task import Task, Result

class vendorController(ABC):


    @abstractmethod
    def testConfig(self) -> Result:
        pass

    @abstractmethod
    def deployConfig(self):
        pass


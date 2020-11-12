from controllers.ios.iosController import iosController
from controllers.mikrotik_routeros.routerosController import routerosController
from controllers.hp_comware.hpController import hpController
from models.Model import Model
from nornir.core.task import Task, Result

class vendorFabric():

    def __init__(self , task: Task , model: Model ):
        self.controller = self._getController(task.host.platform , task , model)
    

    def getController(self):
        return self._controller

     
    def _getController(self, platform, task , model):
        if(platform == 'ios' ):
            return iosController(task=task , model=model)
        if(platform == 'mikrotik_routeros'):
            return routerosController(task=task , model=model)
        if(platform == 'hp_comware'):
            return hpController(task=task , model=model)



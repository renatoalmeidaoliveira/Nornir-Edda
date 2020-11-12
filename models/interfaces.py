from models.Model import Model
from models.Model import ModelSyntaxError
from models.interface import InterfaceModel



class InterfacesModel(Model):

    def __init__(self, interfaces=None):
        self.model = 'interfaces'
        self.interfaces = interfaces
        self._lintModel()

    def _lintModel(self):
        if(type(self.interfaces) != type([])):
            raise ModelSyntaxError("Wrong interfaces type, MUST be list")
        if(len(self.interfaces) ==0):
            raise ModelSyntaxError("empty Interfaces")
        else:
            for interface in self.interfaces:
                if( not isinstance(interface, InterfaceModel)):
                    raise ModelSyntaxError("Wrong Interface Type")


    def getModel(self):
        return self.model

    def getModelData(self):
        model = {}
        ifaces = []
        for interface in self.interfaces:
            ifaces.append(interface.getModelData())
        model['interfaces'] = ifaces
        return model


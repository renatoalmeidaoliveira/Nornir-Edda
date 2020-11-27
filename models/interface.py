from models.Model import Model
from models.Model import ModelSyntaxError
import ipaddress


class InterfaceModel(Model):

    def __init__(self, name=None, description=None, ipv4=None, enabled=False):
        self.model = 'ietf-interface'
        self.name = name
        self.description = description
        self.ipv4 = ipv4
        self.enabled = enabled
        self._lintModel()

    def _lintModel(self):
        if(self.name == None):
            raise ModelSyntaxError("Empty interface Name")
        if(self.ipv4 is not None):
           if(type(self.ipv4) != type([])):
                raise ModelSyntaxError("Wrong ipv4 type, MUST be list")
           if(len(self.ipv4) != 0):
               for ip in self.ipv4:
                   if(not 'prefix_length' in ip):
                       raise ModelSyntaxError("IPv4 without prefix_length")
                   if((ip['prefix_length'] > 32) or (ip['prefix_length'] < 0)):
                       raise ModelSyntaxError("Invalid prefix_length")
                   ip_address = ipaddress.ip_interface(f"{ip['ip']}/{ip['prefix_length']}")
                   if(ip_address.ip == ip_address.network.network_address):
                       raise ModelSyntaxError("Invalid IP for network mask")
                   if(ip_address.ip == ip_address.network.broadcast_address):
                       raise ModelSyntaxError("Invalid IP for network mask")

    def getModel(self):
        return self.model

    def getModelData(self):
        model = {}
        model['name'] = self.name
        model['enabled'] = self.enabled
        if(self.description != None):
            model['description'] = self.description
        if(self.ipv4 is not None):
            if(len(self.ipv4) != 0):
                adressess = {}
                adressess['address'] = self.ipv4
                model['ipv4'] = adressess
        return model


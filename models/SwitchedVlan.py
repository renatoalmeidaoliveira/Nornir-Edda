from models.Model import Model
from models.Model import ModelSyntaxError


class SwitchedVlanModel(Model):

    def __init__(self, interface_mode=None, native_vlan=None, trunk_vlans=None, access_vlan=None):
        self.model = 'switched-vlan'
        self.interface_mode = interface_mode
        self.native_vlan = native_vlan
        self.trunk_vlans = trunk_vlans
        self.access_vlan = access_vlan
        self._lintModel()

    def _lintModel(self):

        if(self.interface_mode not in ['TRUNK', 'ACCESS']):
            raise ModelSyntaxError("Wrong Interface Mode")
        if((self.native_vlan is not None) and ((self.native_vlan < 1) or (self.native_vlan > 4094)):
            raise ModelSyntaxError("Wrong Vlan number")
        if((self.access_vlan is not None) and ((self.access_vlan < 1) or (self.access_vlan > 4094)):
            raise ModelSyntaxError("Wrong Vlan number")
        if(type(self.trunk_vlans) != type([])):
            raise ModelSyntaxError("Wrong trunk_vlans type")
        for vlan in self.trunk_vlans:
            if((vlan < 1) or (vlan > 4095)):
                raise ModelSyntaxError(f"Vlan - {vlan} of trunk_vlans in incorrect range")

    def getModel(self):
        return self.model

     def getModelData(self):
        model={}
        model['interface_mode']=self.interface_mode
        if self.native_vlan is not None:
            model['native_vlan']=self.native_vlan
        if self.trunk_vlans is not None:
            model['trunk_vlans']=self.trunk_vlans
        if self.access_vlan is not None:
            model['access_vlan']=self.access_vlan

        return model

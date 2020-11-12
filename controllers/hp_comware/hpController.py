from controllers.Controller import vendorController
from jinja2 import Environment, PackageLoader
from models.Model import Model
from nornir.core.task import Task, Result
from nornir_netmiko.connections import CONNECTION_NAME


def cidr_to_netmask(cidr):
  cidr = int(cidr)
  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
  return (str( (0xff000000 & mask) >> 24)   + '.' +
          str( (0x00ff0000 & mask) >> 16)   + '.' +
          str( (0x0000ff00 & mask) >> 8)    + '.' +
          str( (0x000000ff & mask)))


class hpController(vendorController):

    def __init__(self , task: Task , model: Model):
        self.task = task
        self.model = model

    def _generateConfig(self):
        env = Environment(loader=PackageLoader('controllers.hp_comware', 'templates'))
        env.filters['cidr_to_netmask'] = cidr_to_netmask
        templ = env.get_template(f"{self.model.getModel()}.j2")
        config = templ.render(self.model.getModelData())
        configs = config.split('\n')
        while( '' in configs ):
            configs.remove('')
        return configs


    def testConfig(self) -> Result:
        configs = self._generateConfig()
        return Result(
                host= self.task.host,
                result= configs
            )

    def deployConfig(self) -> Result:
        configs = self._generateConfig()
        net_connect = self.task.host.get_connection(CONNECTION_NAME, self.task.nornir.config)
        result = net_connect.send_config_set(configs)
        return Result(
                host= self.task.host,
                result= result
            )

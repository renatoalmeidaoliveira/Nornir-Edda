from controllers.Controller import vendorController
from jinja2 import Environment, PackageLoader
from models.Model import Model
from nornir.core.task import Task, Result
from nornir_napalm.plugins.tasks import napalm_configure
import ipaddress


def cidr_to_netmask(cidr):
  cidr = int(cidr)
  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
  return (str( (0xff000000 & mask) >> 24)   + '.' +
          str( (0x00ff0000 & mask) >> 16)   + '.' +
          str( (0x0000ff00 & mask) >> 8)    + '.' +
          str( (0x000000ff & mask)))


class iosController(vendorController):

    def __init__(self , task: Task , model: Model):
        self.task = task
        self.model = model

    def _generateConfig(self):
        env = Environment(
            loader=PackageLoader('controllers.ios', 'templates'),
            line_statement_prefix='#'
        )
        env.filters['cidr_to_netmask'] = cidr_to_netmask
        templ = env.get_template(f"{self.model.getModel()}.j2")
        config = templ.render(self.model.getModelData())
        return config


    def testConfig(self) -> Result:
        return Result(
                host= self.task.host,
                result= self._generateConfig()
            )

    def deployConfig(self) -> Result:
        config = self._generateConfig()
        result = self.task.run(
            name= f"Device Configuration",
            task= napalm_configure,
            configuration=config
        )
        return result



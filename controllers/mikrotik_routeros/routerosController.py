from controllers.Controller import vendorController
from jinja2 import Environment, PackageLoader
from models.Model import Model
from nornir.core.task import Task, Result
from nornir_netmiko.connections import CONNECTION_NAME

class routerosController(vendorController):

    def __init__(self , task: Task , model: Model):
        self.task = task
        self.model = model

    def _generateConfig(self):
        env = Environment(loader=PackageLoader('controllers.mikrotik_routeros', 'templates'))
        templ = env.get_template(f"{self.model.getModel()}.j2")
        config = templ.render(self.model.getModelData())
        configs = config.split('\n')
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
        results = []
        for command in configs:
            result = net_connect.send_command(command)
            results.append(result)
        return Result(
                host= self.task.host,
                result= results
            )

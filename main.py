from nornir import InitNornir
import os
import pprint
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml
from models.interface import InterfaceModel
from models.interfaces import InterfacesModel
from controllers.Fabric import vendorFabric

def loadData(task: Task) -> Result:
    cwd = os.getcwd()
    data = task.run(
        name= f"{task.host.name} dataModel",
        task= load_yaml,
        file=f"{cwd}/data/{task.host.name}/interface.yaml"
    )
    interfaces = data.result
    ifaces = []
    for interface in interfaces['interfaces']:
        iface = InterfaceModel(
                               name=interface['name'],
                               description=interface['description'],
                               ipv4=interface['ipv4']['address'],
                               enabled=interface['enabled'] if 'enabled' in interface else False)
        ifaces.append(iface)
    interfaces = InterfacesModel(interfaces=ifaces)
    controller = vendorFabric(task=task, model=interfaces).controller
    return controller.testConfig()



nr = InitNornir()

load_models = nr.run(
    name="Load Models",
    task= loadData
)

print_result(load_models)

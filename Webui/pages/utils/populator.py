from platform import system
import glob
from yaml import load, SafeLoader, FullLoader
from pprint import pprint

def marker(_type: str):
    """ Der marker ist dafür da, genau zu bestimmen, wie viele datein in der Gui angezeigt werden müssen.
        Auf einfrage eines bestimmten typs, gibt der loader die anzahl unterschiedlicher datein zurück.
        :_type: [str]  Bestimmt den typ der anfrage (inventory, playbooks, config)
    """
    if system() == "Windows":
        path_ansible_dir = r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\ansible-cfg"
    else:
        path_ansible_dir = r"/home/nick/Ansible-Website/ansible-cfg/"
    if _type == "inventory":
        list_of_files = glob.glob(path_ansible_dir + "\\inventory\\*.yml")
        return list_of_files
    if _type == "playbooks":
        list_of_files = glob.glob(path_ansible_dir + "\\playbooks\\*.yml")
        return list_of_files
    if _type == "config":
        list_of_files = glob.glob(path_ansible_dir + "\\*.cfg")
        return list_of_files


def informer(path: str, tag="a"):
    """ Oeffnet Datein und gibt ihren inhalt zurück.
        :path: [str] pfad zur datei
    """
    stream = open(path)
    _yaml = load(stream=stream, Loader=FullLoader)
    return _yaml


# pprint(informer(r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Test\playbooks\update_via_http.yml"))

_list = []
with open(r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Test\playbooks\update_via_http.yml") as _file:
    print(_file)
    for line in _file:
        _list.append(_file.readline())

pprint(_list)



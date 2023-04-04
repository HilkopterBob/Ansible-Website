from platform import system
import glob
import ntpath

async def finder():
    pass

def populator(inventory = False, playbooks = False,  inventory_names = [], playbook_names = [], cfg = False):
    """ gets requested info from files of the ansible-cfg dir. returns info as list of dicts 
    
        :inventory: Flag, if true and no inventory_names will return all infos from all inventorys.
                    if inventory_names > 0: will return infos only from requested files.
        :inventory_names: list of strings, containing files names. Only for specific requests.
        :playbook: Flag, if true and no playbook_names will return all infos from all playbooks.
                    if playbook_names > 0: will return infos only from requested files.
        :playbook_names: list of strings, containing files names. Only for specific requests.
        :cfg: will return infos about the cfg

    """
    if system() == "Windows":
        path_ansible_dir = r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\ansible-cfg"
    else:
        path_ansible_dir = r"/home/nick/Ansible-Website/ansible-cfg/"

    if inventory and len(inventory_names) == 0:
        list_of_infos = []
        list_of_files = glob.glob(path_ansible_dir + "\\inventory\\*.yml")
        for path in list_of_files:
            _file = open(path)
            list_of_infos.append({f"{ntpath.basename(path)}":{}})
            for index, line in enumerate(_file):
                list_of_infos[0][ntpath.basename(path)]
    if inventory and len(inventory_names) > 0:
        pass
    if playbooks and len(playbook_names) == 0:
        pass
    if playbooks and len(playbook_names) > 0:
        pass
    if cfg:
        pass
    
populator(True)









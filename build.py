import os
import subprocess
from pathlib import Path
import nicegui

cmd = [
    'python',
    '-m', 'PyInstaller',
    'C:\\Users\\npodewils\\Desktop\\p\\C.D.Buettner\\Ansible-Website\\Webui\\webui.py', # your main file with ui.run()
    '--name', 'Ansible Automation Hub', # name of your app
    '--onefile',
    #'--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui',    

]
subprocess.call(cmd)
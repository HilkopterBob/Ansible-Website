from nicegui import ui, app



app.add_static_files("/static", "static")
# import sys
# sys.setrecursionlimit(1000)
#app start↓
from pages import login_page, landing_page, logout, admin_panel


ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")

ui.run(port=80, dark=True, title="Ansible Automation Hub")
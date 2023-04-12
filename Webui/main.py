from nicegui import ui, app, globals
from starlette.middleware.sessions import SessionMiddleware
from fastapi import Request
from typing import Dict
import platform


#from pages import login_page, landing_page, logout, admin_panel
from pages import index, login, admin_panel, logout
import theme


app.add_middleware(SessionMiddleware, secret_key='some_random_string')
session_info: Dict[str, Dict] = {}


app.add_static_files("/static", "static")

@ui.page('/')
async def index_page(request: Request) -> None:
    with theme.frame('Ansible Automation Hub', header=True):
        return await index.content(request, session_info)

@ui.page('/login')
async def login_page(request: Request) -> None:
    with theme.frame(header=False):
        ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")
        return await login.content(request, session_info)

@ui.page('/admin-panel')
async def admin_page(request: Request) -> None:
    with theme.frame("Administration Panel", header=True):
        return await admin_panel.content(request, session_info)

@ui.page('/logout')
async def logout_page(request: Request) -> None:
    with theme.frame(header=False):
        return await logout.content(request, session_info)




if platform.system() == "Windows":
    ui.run(port=80, title="Ansible Automation Hub",\
        favicon=r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\Webui\static\favicon-32x32.png",\
    )
else:
    ui.run(port=80, dark=True, title="Ansible Automation Hub",\
        favicon=r"/home/nick/Ansible-Website/Webui/static/favicon-32x32.png",\
    )


from nicegui import ui, app, globals, Client
from starlette.middleware.sessions import SessionMiddleware
from fastapi import Request
from typing import Dict
import platform


#from pages import login_page, landing_page, logout, admin_panel
from pages import conti, login, admin_panel, logout, intern
import theme

MATPLOTLIB = False

app.add_middleware(SessionMiddleware, secret_key='some_random_string')
session_info: Dict[str, Dict] = {}


app.add_static_files("/static", "static")



@ui.page('/')
async def index_page(request: Request, client: Client) -> None:
    with theme.frame(client, _session_info=session_info, navtitle='Ansible Automation Hub Contipark', header=True):
        return await conti.content(request, session_info, client=client)

@ui.page('/intern')
async def index_page(request: Request, client: Client) -> None:
    with theme.frame(client, _session_info=session_info, navtitle='Ansible Automation Hub C.D. Büttner', header=True):
        return await intern.content(request, session_info, client=client)

@ui.page('/login')
async def login_page(request: Request, client: Client) -> None:
    with theme.frame(client, _session_info=session_info, header=False):
        ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")
        return await login.content(request, session_info, client=client)

@ui.page('/admin-panel')
async def admin_page(request: Request, client: Client) -> None:
    with theme.frame(client, _session_info=session_info, navtitle="Administration Panel", header=True):
        return await admin_panel.content(request, session_info, client=client)

@ui.page('/logout')
async def logout_page(request: Request, client: Client) -> None:
    with theme.frame(client, _session_info=session_info, header=False):
        return await logout.content(request, session_info)



if __name__ in {"__main__", "__mp_main__"}:
    if platform.system() == "Windows":
        ui.run(port=80, dark=True, title="Ansible Automation Hub",\
            favicon=r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\Webui\static\favicon-32x32.png",\
        )
    else:
        ui.run(port=80, dark=True, title="Ansible Automation Hub",\
            favicon=r"/home/nick/Ansible-Website/Webui/static/favicon-32x32.png",\
        )
    
    
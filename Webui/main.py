from nicegui import ui, app
from starlette.middleware.sessions import SessionMiddleware
from fastapi import Request
from typing import Dict


#from pages import login_page, landing_page, logout, admin_panel
from pages import index, login, admin_panel, logout
import theme


app.add_middleware(SessionMiddleware, secret_key='some_random_string')
session_info: Dict[str, Dict] = {}


app.add_static_files("/static", "static")

@ui.page('/')
async def index_page(request: Request) -> None:
    with theme.frame('Ansible Automation Hub', header=True):
        await index.content(request, session_info)

@ui.page('/login')
async def login_page(request: Request) -> None:
    with theme.frame():
        await login.content(request, session_info)

@ui.page('/admin-panel')
async def admin_page(request: Request) -> None:
    with theme.frame("Administration Panel", header=True):
        await admin_panel.content(request, session_info)

@ui.page('/logout')
async def logout_page(request: Request) -> None:
    with theme.frame():
        await logout.content(request, session_info)







ui.run(port=80, dark=True, title="Ansible Automation Hub",\
    favicon=r"./static/favicon-32.32.png",\
)
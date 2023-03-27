from nicegui import ui, app
from typing import Dict
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware



app.add_middleware(SessionMiddleware, secret_key='some_random_string')  # use your own secret key here

users = [('nick', ''), ('user2', 'pass2')]
session_info: Dict[str, Dict] = {}

def is_authenticated(request: Request) -> bool:
    return session_info.get(request.session.get('id'), {}).get('authenticated', False)


@ui.page('/')
def landng_page(request: Request) -> None:
    if not is_authenticated(request):
        return RedirectResponse('/login')
    session = session_info[request.session['id']]
    with ui.header().classes("flex flex-wrap items-center justify-between w-full justify-self-center"):
        with ui.row().classes("w-full p-0"):
            with ui.row().classes('flex items-center self-center'):
                ui.label("büttnerlogo")
            ui.label("").classes("w-10/12")
            with ui.row().classes('grid justify-self-end'):
                with ui.tabs() as tabs:
                    ui.tab('Home', icon='home')
                    ui.tab('About', icon='info')
        
    with ui.tab_panels(tabs, value='Home').classes('absolute-center w-full h-full'):
        with ui.tab_panel('Home'):
            ui.label('This is the first tab')
        with ui.tab_panel('About'):
            ui.label('This is the second tab')
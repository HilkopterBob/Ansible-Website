from nicegui import ui, app
from typing import Dict
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import itertools
from .components import listitem
from time import sleep



app.add_middleware(SessionMiddleware, secret_key='some_random_string')  # use your own secret key here

users = [('nick', ''), ('user2', 'pass2')]
admins = [("admin", r"!t6S%cB2nyTY8nmd0w4t!v0fxLvKMPYFKR3LJf9kFMMC34h*Ch")]
session_info: Dict[str, Dict] = {}




def is_authenticated(request: Request) -> bool:
    return session_info.get(request.session.get('id'), {}).get('authenticated', False)


@ui.page('/')
def landing_page(request: Request) -> None:
    ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")
    if not is_authenticated(request):
        return RedirectResponse('/login')
    session = session_info[request.session['id']]


    # ================ Header ================ #
    with ui.header().style("background-color: #1d1d1d").classes("items-center justify-between"):
                ui.image("/static/buettner-nice-removebg-preview.png").style("width:150px; height:50px")
                ui.label('Ansible Automation Hub').style('''
                                                background: linear-gradient(to right, #BB86FC, #03DAC5);
                                                -webkit-background-clip: text;
                                                -webkit-text-fill-color: transparent;
                                                ''').classes("text-h5")
                with ui.row():
                    ui.button(on_click=lambda: right_drawer.toggle()).props("icon=menu outline")

    with ui.right_drawer(value=False, fixed=False).style('background-color: #1d1d1d').props('bordered') as right_drawer:
        with ui.expansion("Account", icon="person"):
            ui.label(" ")
            ui.button("settings", on_click=lambda: ui.open("/settings")).classes("w-full").props("align=left outline icon=logout")
            ui.button("log out", on_click=lambda: ui.open("/logout")).classes("w-full").props("align=left outline icon=logout")
        with ui.expansion("Docs", icon="person"):
            ui.label(" ")
            ui.button("Open Docs", on_click=lambda: ui.open("/settings")).classes("w-full").props("align=left outline icon=logout")
            with ui.expansion("Paragraphs", icon="person").props("header-inset-level=1"):
                ui.label(" ")
                ui.button("settings", on_click=lambda: ui.open("/settings")).classes("w-full").props("align=left outline icon=logout")
                ui.button("log out", on_click=lambda: ui.open("/logout")).classes("w-full").props("align=left outline icon=logout")
    
    # ~~~~~ Main Page Preset Builder Card ~~~~~ #

    with ui.card().classes(" w-full") as card: #absolute-center w-full h-full
        with ui.tabs().props("indicator-color=transparent") as tabs:
            ui.tab('Presets', icon='description')
            ui.tab('Builder', icon='edit_document')
        
        with ui.tab_panels(tabs, value='Home').classes("w-full"):
            with ui.tab_panel('Presets'):
                # inside the Presets tab
                with ui.column().classes("w-full") as col:
                #für jede zeile im log wird ein listitem generiert
                #falls mehr als 50 zeilen generiert wurden, wird unten die möglichkeit gegeben
                #eine seite weiter zu blättern und die nächsten 50 items zu sehen
                    with col:
                        for _ in itertools.repeat(None, 5): listitem()
            with ui.tab_panel('Builder'):
                ui.label('This is the second tab')


    # ~~~~~ Main Page running history Card  ~~~~~ #

    with ui.card().classes(" w-full") as card: #absolute-center w-full h-full
        with ui.tabs().props("indicator-color=transparent") as tabs:
            ui.tab('Jobs', icon='developer_board')
            ui.tab('History', icon='verified')
        
        with ui.tab_panels(tabs, value='Home').classes("w-full"):
            with ui.tab_panel('Jobs'):
                ui.label('This is the first tab')
            with ui.tab_panel('History'):
                ui.label('This is the second tab')

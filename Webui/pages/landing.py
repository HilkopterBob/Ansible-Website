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
    ui.colors(primary="#BB86FC")
    if not is_authenticated(request):
        return RedirectResponse('/login')
    session = session_info[request.session['id']]


    # ================ Landing Page ================ #
    with ui.header().style("background-color: #1d1d1d").classes("items-center justify-between"):
                ui.image("http://127.0.0.1:3000/buettner-nice-removebg-preview.png").style("width:150px; height:50px")
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
            with ui.expansion("Paragraphs", icon="person"):
                ui.label(" ")
                ui.button("settings", on_click=lambda: ui.open("/settings")).classes("w-full").props("align=left outline icon=logout")
                ui.button("log out", on_click=lambda: ui.open("/logout")).classes("w-full").props("align=left outline icon=logout")
    with ui.card().style("background-color:#BB86FC").classes("") as card:
        with ui.row() as row:
            with ui.column() as col:
                ui.label("Automate IT!").style("color:#03DAC5").classes("text-h6")


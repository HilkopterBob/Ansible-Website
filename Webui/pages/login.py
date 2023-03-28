from nicegui import ui, app
from typing import Dict
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
import uuid
from .landing import is_authenticated, session_info, users, admins



@ui.page('/login')
def login_page(request: Request) -> None:
    ui.colors(primary="#BB86FC")
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if (username.value, password.value) in admins:
            session_info[request.session['id']] = {'username': username.value, 'authenticated': True}
            ui.open('/admin-panel')
        if (username.value, password.value) in users:
            session_info[request.session['id']] = {'username': username.value, 'authenticated': True}
            ui.open('/')
        else:
            ui.notify('Wrong username or password', color='negative')
            username.value = ""
            password.value = ""



    if is_authenticated(request):
        return RedirectResponse('/')
    request.session['id'] = str(uuid.uuid4())  # this stores a new session ID in the cookie of the client
    with ui.card().classes('absolute-center'):
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password').props('type=password').on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login).props("outline")
from nicegui import ui, app
from typing import Dict
from fastapi import Request
from fastapi.responses import RedirectResponse
import uuid
from asyncio import sleep


from .utils.auth import is_authenticated, users, admins


async def content(request: Request, session_info) -> None:
    async def try_login() -> None:  # local function to avoid passing username and password as arguments
        if (username.value, password.value) in admins:
            session_info[request.session['id']] = {'username': username.value, 'authenticated': True, 'admin': True}
            ui.open('/admin-panel')
        if (username.value, password.value) in users:
            session_info[request.session['id']] = {'username': username.value, 'authenticated': True}
            ui.open('/')
        else:
            ui.notify('Wrong username or password', color='negative')
            username.value = ""
            password.value = ""

    if await is_authenticated(request, session_info):
        return ui.open('/')
    request.session['id'] = str(uuid.uuid4())  # this stores a new session ID in the cookie of the client
    request.session['color_scheme'] = "color_scheme"
    session_info[request.session['color_scheme']] = {'dark_mode':True}

    with ui.card().classes('absolute-center'):
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password').props('type=password').on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login).props("outline")
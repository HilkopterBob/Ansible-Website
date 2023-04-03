from nicegui import ui, app
from fastapi import Request
from contextlib import contextmanager
from starlette.middleware.sessions import SessionMiddleware
from typing import Dict
from fastapi.responses import RedirectResponse

app.add_middleware(SessionMiddleware, secret_key='some_random_string')
session_info: Dict[str, Dict] = {}
users = [('user', '')]

@contextmanager
def frame():
    '''Custom page frame to share the same styling and behavior across all pages'''
    ui.button("Frame button")
    with ui.element("div").classes(" w-full"):
        yield

async def is_authenticated(request: Request, session_info) -> bool:
    return session_info.get(request.session.get('id'), {}).get('authenticated', False)

@ui.page('/')
async def index_page(request: Request) -> None:
    with frame():
        await content(request, session_info)

async def content(request: Request, session_info) -> None:
    if not await is_authenticated(request, session_info):  
        return RedirectResponse('/login')  
    ui.button("Content")

@ui.page('/login')
async def index_page(request: Request) -> None:
    ui.button("login")

ui.run()
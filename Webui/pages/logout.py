from nicegui import ui, app
from typing import Dict
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


from .utils import is_authenticated


@ui.page('/logout')
async def content(request: Request, session_info) -> None:
    try:
            session_info.pop(request.session['id'])
            request.session['id'] = None
    except:
        pass
    return RedirectResponse('/login')
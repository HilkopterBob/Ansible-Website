from nicegui import ui
from fastapi import Request
from fastapi.responses import RedirectResponse

from .utils import is_authenticated


async def content(request: Request, session_info) -> None :
    # if not is_authenticated(request, session_info):
    #     return RedirectResponse('/login')
    ui.label("admin panel")
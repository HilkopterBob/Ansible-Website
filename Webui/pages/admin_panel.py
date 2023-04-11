from nicegui import ui, globals
from fastapi import Request
from fastapi.responses import RedirectResponse
from asyncio import sleep
from .utils.auth import is_authenticated, is_admin



async def content(request: Request, session_info) -> None :
    if not await is_admin(request, session_info): 
        return RedirectResponse('/logout')   
    ui.label("admin panel")
    
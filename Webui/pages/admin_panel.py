from nicegui import ui
from fastapi import Request
from fastapi.responses import RedirectResponse

from .landing import is_authenticated



@ui.page("/admin-panel")
def admin_panel(request: Request) -> None :
    ui.colors(primary="#BB86FC")
    if not is_authenticated(request):
        return RedirectResponse('/login')
    ui.label("admin panel")
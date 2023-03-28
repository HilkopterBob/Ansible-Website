from nicegui import ui
from .landing import is_authenticated, session_info, RedirectResponse
from fastapi import Request

from .conf import primary_color


@ui.page('/logout')
def logout(request: Request) -> None:
    ui.colors(primary=primary_color)
    if is_authenticated(request):
        session_info.pop(request.session['id'])
        request.session['id'] = None
        return RedirectResponse('/login')
    return RedirectResponse('/')
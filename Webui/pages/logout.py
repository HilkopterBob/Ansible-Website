from nicegui import ui
from .landing import is_authenticated, session_info, RedirectResponse
from fastapi import Request



@ui.page('/logout')
def logout(request: Request) -> None:
    if is_authenticated(request):
        session_info.pop(request.session['id'])
        request.session['id'] = None
        return RedirectResponse('/login')
    return RedirectResponse('/')
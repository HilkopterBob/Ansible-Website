from nicegui import ui, globals
from fastapi import Request
from fastapi.responses import RedirectResponse
from asyncio import sleep
from .utils.auth import is_authenticated, is_admin

async def bye():
    for client in globals.clients.values():
        with client:
            ui.notify('Goodbye!', type="warning")


async def content(request: Request, session_info, client) -> None :
    if not await is_admin(request, session_info): 
        return RedirectResponse('/logout')
    
    await client.connected()

    if session_info["color_scheme"]["dark_mode"] == False:
        ui.colors(primary="#FF3300", secondary="#FFFF33", accent="#FFFF33", warning="#FFFF33", info="#FF3300")
        await ui.run_javascript('''
            Quasar.Dark.set(false);
            tailwind.config.darkMode = "class"
            document.body.classList.remove("dark");
        ''', respond=False)
    
    if session_info["color_scheme"]["dark_mode"] == True:
        ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")
        await ui.run_javascript('''
            Quasar.Dark.set(true);
            tailwind.config.darkMode = "class";
            document.body.classList.add("dark");
        ''', respond=False)
    ui.label("admin panel")
    ui.button("byee", on_click=bye)
    
    
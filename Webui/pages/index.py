from nicegui import ui, Client
from fastapi import Request
from fastapi.responses import RedirectResponse



from .utils import is_authenticated








async def content(request: Request, session_info, client: Client) -> None:

    await client.connected()
    try:
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
    except KeyError:
        pass

    if not await is_authenticated(request, session_info):  
        return RedirectResponse("/login")
        ui.label("please log in")
    else:
        ui.label("logged in")
        







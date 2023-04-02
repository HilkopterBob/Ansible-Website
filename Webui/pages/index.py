from nicegui import ui
from fastapi import Request
from fastapi.responses import RedirectResponse
import itertools
from .components import listitem, jobitem

from .utils import is_authenticated











async def content(request: Request, session_info) -> None:
    # if not await is_authenticated(request, session_info):  
    #     return RedirectResponse('/login')    redirectresponse from async not possible as of 1.2.3 see #693


    # ~~~~~ Main Page Preset Builder Card ~~~~~ #

    with ui.card().classes(" w-full") as card: #absolute-center w-full h-full
        with ui.tabs(value="Presets").props("indicator-color=transparent") as tabs:
            ui.tab('Presets', icon='description')
            ui.tab('Builder', icon='edit_document')
        
        with ui.tab_panels(tabs, value="Presets").classes("w-full"):
            with ui.tab_panel('Presets'):
                # inside the Presets tab
                with ui.column().classes("w-full") as col:
                #für jede zeile im log wird ein listitem generiert
                #falls mehr als 50 zeilen generiert wurden, wird unten die möglichkeit gegeben
                #eine seite weiter zu blättern und die nächsten 50 items zu sehen
                    with col:
                        for _ in itertools.repeat(None, 5): listitem()
            with ui.tab_panel('Builder'):
                ui.label('This is the second tab')

    # ~~~~~ End: Main Page Preset Builder Card ~~~~~ #

    ui.label(" ")

    # ~~~~~ Main Page running history Card  ~~~~~ #

    with ui.card().classes(" w-full") as card: #absolute-center w-full h-full
        with ui.tabs(value="Jobs").props("indicator-color=transparent") as tabs:
            ui.tab('Jobs', icon='developer_board')
            ui.tab('History', icon='verified')
        
        with ui.tab_panels(tabs, value='Jobs').classes("w-full"):
            with ui.tab_panel('Jobs'):
                with ui.column().classes("w-full") as col:
                    with col:
                        for _ in itertools.repeat(None, 5): jobitem()
            with ui.tab_panel('History').classes("h-100"):
                with ui.column().classes("w-full h-100"):
                    log = ui.log(max_lines=100).classes("w-full h-96")
                    ui.button("push", on_click=lambda: log.push("hello"))

    # ~~~~~ End: Main Page running history Card  ~~~~~ #
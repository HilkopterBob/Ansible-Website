from nicegui import ui, Client
from fastapi import Request
from fastapi.responses import RedirectResponse
import itertools
from .components import listitem, builder_content, jobitem


from .utils import is_authenticated, populator






def add_jobitem(_object):
    with col_jobitems:
        _object




async def content(request: Request, session_info, client: Client) -> None:
    global col_jobitems
    if not await is_authenticated(request, session_info):  
        return RedirectResponse('/login')
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

    # ~~~~~ Main Page ad-hoc commands Card ~~~~~ #

    # with ui.card().classes("w-full") as card:
    #     ui.label("Ad-hoc Commands:").classes("text-h6")
    #     with ui.row() as row:
    #         with ui.column():
    #             ui.label("")
    #             ui.input()
    #         with ui.column():
    #             ui.select(["IP1", "IP2", "IP3"])
    #         with ui.column():
    #             ui.select(["Backup", "Open Port", "Standard Conf"])


        
        
        

    # ~~~~~ End: Main Page ad-hoc commands Card ~~~~~ #

    ui.label(" ")

    # ~~~~~ Main Page Preset Builder Card ~~~~~ #

    with ui.card().classes(" w-full") as card: #absolute-center w-full h-full
        with ui.tabs(value="Presets").props("indicator-color=transparent") as tabs:
            ui.tab('Presets', icon='description')
            ui.tab('Builder', icon='edit_document')
        
        with ui.tab_panels(tabs, value="Presets").classes("w-full"):
            with ui.tab_panel('Presets'):
                # inside the Presets tab
                with ui.column().classes("w-full") as col:
                    list_of_playbooks = populator.marker("playbooks")
                    for _file in list_of_playbooks:
                        await listitem(_file)
                    
                    
            with ui.tab_panel('Builder').classes("w-full"):
                await builder_content.content()

    # ~~~~~ End: Main Page Preset Builder Card ~~~~~ #

    ui.label(" ")

    # ~~~~~ Main Page running history Card  ~~~~~ #

    with ui.card().classes(" w-full") as card: #absolute-center w-full h-full
        with ui.tabs(value="Jobs").props("indicator-color=transparent") as tabs:
            ui.tab('Jobs', icon='developer_board')
            ui.tab('History', icon='verified')
        
        with ui.tab_panels(tabs, value='Jobs').classes("w-full"):
            with ui.tab_panel('Jobs'):
                with ui.column().classes("w-full") as col_jobitems:
                    for _ in itertools.repeat(None, 5): await jobitem()
            with ui.tab_panel('History').classes("h-100"):
                with ui.column().classes("w-full h-100"):
                    # TODO: für jede zeile im log wird ein listitem generiert
                    #falls mehr als 50 zeilen generiert wurden, wird unten die möglichkeit gegeben
                    #eine seite weiter zu blättern und die nächsten 50 items zu sehen
                    log = ui.log(max_lines=100).classes("w-full h-96")
                    ui.button("push", on_click=lambda: log.push("hello"))

    # ~~~~~ End: Main Page running history Card  ~~~~~ #
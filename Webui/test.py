from contextlib import contextmanager
from nicegui import ui, events

global switch
global dark_mode
global base_row

dark_mode = True

async def start_whitemode():
    await ui.run_javascript('''
                        Quasar.Dark.set(false);
                        tailwind.config.darkMode = "class"
                        document.body.classList.remove("dark");
                    ''', respond=False)

async def start_darkmode():
    await ui.run_javascript('''
                            Quasar.Dark.set(true);
                            tailwind.config.darkMode = "class";
                            document.body.classList.add("dark");
                    ''', respond=False)

def set_color_mode(value: bool, header: ui.header):
    global dark_mode
    if value:
        ui.colors(primary="#BB0000", secondary="#F6F000", accent="#F6F000", warning="#F6F000", info="#BB0000")
        header.style("background-color: #FFFFFFFF")
        for index, element in enumerate(header.default_slot.children):
            if isinstance(element, ui.image):
                header.default_slot.children.pop(index)
        header.default_slot.children.insert(0, ui.image("/static/b-rot.png").style("width:150px; height:50px"))
        events.handle_event(start_whitemode, arguments=None, sender=switch)
        for index, element in enumerate(header.default_slot.children):
            if isinstance(element, ui.row):
                header.default_slot.children.remove(element)
        if switch.id not in header._collect_descendant_ids():
            header.default_slot.children.insert(index, switch)
            print("c1")
        print("c2")
    else:
        ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")
        header.style("background-color: #1d1d1d")
        # if isinstance(header.default_slot.children[0], ui.image):
        #     header.default_slot.children.pop(0)
        for index, element in enumerate(header.default_slot.children):
            if isinstance(element, ui.image):
                header.default_slot.children.pop(index)
        header.default_slot.children.insert(0, ui.image("/static/b-lila.png").style("width:150px; height:50px"))
        events.handle_event(start_darkmode, arguments=None, sender=switch)

        for index, element in enumerate(header.default_slot.children):
            if isinstance(element, ui.row):
                header.default_slot.children.remove(element)
        if switch.id not in header._collect_descendant_ids():
            header.default_slot.children.insert(index, switch)


        # for index, element in enumerate(header.default_slot.children):
        #     if isinstance(element, ui.row):
        #         print(f"{element} is type row on index {index}")
        #         for _index, _element in enumerate(element.default_slot.children):
        #             # if isinstance(_element, ui.colors):
        #             #     element.default_slot.children.pop(_index)
        #             if isinstance(_element, ui.image):
        #                 element.default_slot.children.pop(_index)
        #             print(f"inside the row is following element: {_index} + {_element} ")
        #         print("-"*30)


@contextmanager
def frame(navtitle: str = "foo", header: bool = False):
    '''Custom page frame to share the same styling and behavior across all pages'''
    
    if header:
        fheader(navtitle)
    with ui.element("div").classes(" w-full"):
        yield
def fheader(navtitle: str):
    global  switch
    with ui.header().style("background-color: #1d1d1d").classes("items-center justify-between") as _header:
        ui.label(f'{navtitle}').style('''
                                        background: linear-gradient(to right, #BB86FC, #03DAC5);
                                        -webkit-background-clip: text;
                                        -webkit-text-fill-color: transparent;
                                        ''').classes("text-h5 absolute-center")
        with ui.row():
            switch = ui.switch("White mode", value=False, on_change=lambda: set_color_mode(switch.value, _header))
            ui.button(on_click=lambda: right_drawer.toggle()).props("icon=menu outline")

    with ui.right_drawer(value=False, fixed=False).style('background-color: #1d1d1d').props('bordered') as right_drawer:
        with ui.expansion("Account", icon="person"):
            ui.label(" ")
            ui.button("settings", on_click=lambda: ui.open("/settings")).classes("w-full").props("align=left outline icon=logout")
            ui.button("log out", on_click=lambda: ui.open("/logout")).classes("w-full").props("align=left outline icon=logout")
        with ui.expansion("Docs", icon="person"):
            ui.label(" ")
            ui.button("Open Docs", on_click=lambda: ui.open("/settings")).classes("w-full").props("align=left outline icon=logout")
            with ui.expansion("Paragraphs", icon="person").props("header-inset-level=1"):
                ui.label(" ")
                ui.button("settings", on_click=lambda: ui.open("/settings")).classes("w-full").props("align=left outline icon=logout")
                ui.button("log out", on_click=lambda: ui.open("/logout")).classes("w-full").props("align=left outline icon=logout")
    return _header
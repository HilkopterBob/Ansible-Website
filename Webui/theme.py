from contextlib import contextmanager


from nicegui import ui, events

global _header
global switch
global session_info
dark_mode = True

async def make_dark():
    ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")
    await ui.run_javascript('''
        Quasar.Dark.set(true);
        tailwind.config.darkMode = "class";
        document.body.classList.add("dark");
    ''', respond=False)

async def make_light():
    ui.colors(primary="#FF3300", secondary="#FFFF33", accent="#FFFF33", warning="#FFFF33", info="#FF3300")
    await ui.run_javascript('''
        Quasar.Dark.set(false);
        tailwind.config.darkMode = "class"
        document.body.classList.remove("dark");
    ''', respond=False)


async def set_color_mode():
    global _header
    global session_info

    session_info["color_scheme"]["dark_mode"] = not session_info["color_scheme"]["dark_mode"] 

    if session_info["color_scheme"]["dark_mode"] == True:
        events.handle_event(make_dark, arguments=None, sender=switch)
    if session_info["color_scheme"]["dark_mode"] == False:
        events.handle_event(make_light, arguments=None, sender=switch)
    return fheader(navtitle="Ansible Automation Hub", session_info=session_info)

@contextmanager
def frame(_session_info, navtitle: str = "foo", header: bool = False):
    global session_info
    session_info = _session_info
    '''Custom page frame to share the same styling and behavior across all pages'''
    try:
        if session_info["color_scheme"]["dark_mode"] == True:
            ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")
        elif session_info["color_scheme"]["dark_mode"] == False:
            pass
    except KeyError as e:
        print(e)
    if header:
        fheader(navtitle, session_info)
    with ui.element("div").classes(" w-full"):
        yield

def fheader(navtitle: str, session_info):
    global _header
    global switch
    try:
        if session_info["color_scheme"]["dark_mode"] == True:
            with ui.header().style("background-color: #1d1d1d").classes("items-center justify-between") as _header:
                        ui.image("/static/b-lila.png").style("width:150px; height:50px")
                        ui.label(f'{navtitle}').style('''
                                                        background: linear-gradient(to right, #BB86FC, #03DAC5);
                                                        -webkit-background-clip: text;
                                                        -webkit-text-fill-color: transparent;
                                                        ''').classes("text-h5 absolute-center")
                        with ui.row():
                            switch = ui.switch("Dark Mode", value=True, on_change=set_color_mode)
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
    
        elif session_info["color_scheme"]["dark_mode"] == False:
            with ui.header().style("background-color: #FFFFFF").classes("items-center justify-between") as _header:
                        ui.image("/static/b-rot.png").style("width:150px; height:50px")
                        ui.label(f'{navtitle}').style('''
                                                        background: linear-gradient(to right, #FF3300, #FFFF33);
                                                        -webkit-background-clip: text;
                                                        -webkit-text-fill-color: transparent;
                                                        ''').classes("text-h5 absolute-center")
                        with ui.row():
                            ui.switch("Dark Mode", value=False, on_change=set_color_mode).props("outline").style(add="color:#000000").set_visibility("true")
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
    except KeyError as e:
        print(e)
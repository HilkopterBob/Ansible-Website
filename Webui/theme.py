from contextlib import contextmanager


from nicegui import ui


@contextmanager
def frame(navtitle: str = "foo", header: bool = False):
    '''Custom page frame to share the same styling and behavior across all pages'''
    
    ui.colors(primary="#BB86FC", secondary="#03DAC5", accent="#03DAC5", warning="#03DAC5", info="#BB68FC")
    if header:
        fheader(navtitle)
    with ui.element("div").classes(" w-full"):
        yield

def fheader(navtitle: str):
    with ui.header().style("background-color: #1d1d1d").classes("items-center justify-between") as _header:
                ui.image("/static/buettner-nice-removebg-preview.png").style("width:150px; height:50px")
                ui.label(f'{navtitle}').style('''
                                                background: linear-gradient(to right, #BB86FC, #03DAC5);
                                                -webkit-background-clip: text;
                                                -webkit-text-fill-color: transparent;
                                                ''').classes("text-h5 absolute-center")
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
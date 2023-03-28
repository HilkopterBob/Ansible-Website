from nicegui import ui






def listitem():
    #creates line shaped container
    with ui.expansion("").classes("w-full").props("expand-icon-toggle popup") as Listitem:
        with Listitem.add_slot("header"):
            # alles in eine row packen und die dann ober mega groß machen
            with ui.row().classes("w-full items-center justify-between"):
                ui.label("playbok name")
                ui.label("hosts")
                with ui.row():
                    ui.button("").props("icon=play_arrow")
                    ui.button("").props("icon=edit")
        with ui.card().classes("w-full"):
            ui.label("inside the expansion")
    return Listitem






































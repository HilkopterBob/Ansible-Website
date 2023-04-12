from nicegui import ui

async def jobitem(name, last_run="[LOGABFRAGE wann letztes mal gestartet]"):
    #creates line shaped container
    with ui.expansion("").classes("w-full").props("expand-icon-toggle popup") as Jobitem:
        with Jobitem.add_slot("header"):
            # alles in eine row packen und die dann ober mega groß machen
            with ui.row().classes("w-full items-center justify-between"):
                ui.label(name)
                ui.label(last_run)
                with ui.row():
                    ui.spinner(type="ios").props("size=md")
                    ui.button("").props("icon=close outline")
        with ui.card().classes("w-full") as card:
                            with ui.row().classes("w-full items-center justify-between") as row:
                                with ui.card().classes("w-full") as card:
                                    with ui.row().classes("w-full"):
                                        ui.label("Name:")
                                        ui.label("%%name%%")
                                    with ui.row().classes("w-full"):
                                        ui.label("Descr:")
                                        ui.label("%%descr%%")
                                with ui.card().classes("w-full") as card:
                                    with ui.row().classes("w-full"):
                                        ui.label("Parameter:")
                                        with ui.row().classes("w-full items-center"):
                                            ui.label("param1:")         #zb. backuppatch
                                            ui.input()
                                        with ui.row().classes("w-full items-center"):
                                            ui.label("param2:")         #zb. backuppatch
                                            ui.input()
                                        with ui.row().classes("w-full items-center"):
                                            ui.label("param3:")         #zb. backuppatch
                                            ui.input()
        with ui.card().classes("w-full h-96") as card:
            log = ui.log(max_lines=100).classes("w-full h-96")
    return Jobitem


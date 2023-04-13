from nicegui import ui
from platform import system



async def listitem(_file):
    #creates line shaped container
    with ui.expansion("").classes("w-full").props("expand-icon-toggle popup bordered") as Listitem:
        with Listitem.add_slot("header"):
            # alles in eine row packen und die dann ober mega groß machen
            with ui.row().classes("w-full items-center justify-between"):
                if system() == "Windows":
                    ui.label(_file.replace("_", " ").split("\\")[-1].replace(".yml", ""))
                else:
                    ui.label(_file.replace("_", " ").split("/")[-1])
                ui.label("[Suche nach der letzten gelaufenen wiederholung im log !!!]").classes("absolute-center") #call search_in_log(func_name)
                with ui.row():
                    ui.button("", on_click= lambda: start_playbook(_file, Listitem)).props("icon=play_arrow outline")
                    ui.button("").props("icon=edit outline")
        with ui.card().classes("w-full") as card:
                            with open(_file, "r") as file:
                                data = file.read()
                            ui.markdown(f''' ```yaml
{data} ``` ''')
    return Listitem






































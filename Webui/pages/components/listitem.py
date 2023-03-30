from nicegui import ui
from functools import partial
from .searchbars import sayt, get_checked_results, sayt_copy



def hosts_changed_values(changed_component, second_component, third_component):
    if changed_component.value != False:
        second_component.set_value(not changed_component.value)
        third_component.set_value(not changed_component.value)
    if changed_component.value == False and second_component.value == False and third_component.value == False:
        ui.notify("must select host-type", type="info")


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
                                with ui.card().classes("w-full") as card:
                                    with ui.row().classes("w-full"):
                                        with ui.row().classes("w-full"):
                                            ui.label("Hosts:")
                                        with ui.row().classes("w-full items-center"):    
                                            host_all = ui.checkbox("all", value=True).on("click", lambda: hosts_changed_values(host_all, host_groups, host_individual))
                                            host_groups = ui.checkbox("groups", value=False).on("click", lambda: hosts_changed_values(host_groups, host_all, host_individual))      
                                            host_individual = ui.checkbox("individual IP", value=False).on("click", lambda: hosts_changed_values(host_individual, host_all, host_groups))
                                        with ui.column().classes("w-full items-center").bind_visibility_from(host_groups, "value"):
                                            #searchbar = sayt(r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\Webui\csv's\lookup.csv")
                                            checked_values = sayt(r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\Webui\csv's\lookup.csv")
                                            print(checked_values)
                                            # results[0]
                                            # results[1]
                                            # searchbar.on_value_change(print(f"changed!! {searchbar.value}"))
                                            # # with ui.column().classes("w-full items-left"):
                                            # #     checked_results = get_checked_results()
                                            # #     for item in checked_results:
                                            # #         ui.label(item)
                                            # print(searchbar.default_slot.children)
                                        with ui.column().classes("w-full items-center").bind_visibility_from(host_individual, "value"):
                                            searchbar = sayt_copy(r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\Webui\csv's\lookup.csv")
    return Listitem






































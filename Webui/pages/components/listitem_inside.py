from nicegui import ui
from utils import populator






async def listitem_inside(index):
    
    with ui.column().classes("w-full")as column:






        # with ui.card().classes("w-full") as card:
        #     with ui.row().classes("w-full items-center justify-between") as row:
        #         with ui.card().classes("w-full") as card:
        #             with ui.row().classes("w-full"):
        #                 ui.label("Name:")
        #                 ui.label("%%name%%")
        #             with ui.row().classes("w-full"):
        #                 ui.label("Descr:")
        #                 ui.label("%%descr%%")
        #         with ui.card().classes("w-full") as card:
        #             with ui.row().classes("w-full"):
        #                 ui.label("Tasks:")
        #                 with ui.row().classes("w-full items-center"):
        #                     ui.label("param1:")         #zb. backuppatch
        #                     ui.input()
        #                 with ui.row().classes("w-full items-center"):
        #                     ui.label("param2:")         #zb. backuppatch
        #                     ui.input()
        #                 with ui.row().classes("w-full items-center"):
        #                     ui.label("param3:")         #zb. backuppatch
        #                     ui.input()
        # with ui.card().classes("w-full") as card:
        #     with ui.row().classes("w-full"):
        #         with ui.row().classes("w-full"):
        #             ui.label("Hosts:")
        #         with ui.row().classes("w-full items-center"):    
        #             host_all = ui.checkbox("all", value=True).on("click", lambda: hosts_changed_values(host_all, host_groups, host_individual))
        #             host_groups = ui.checkbox("groups", value=False).on("click", lambda: hosts_changed_values(host_groups, host_all, host_individual))      
        #             host_individual = ui.checkbox("individual IP", value=False).on("click", lambda: hosts_changed_values(host_individual, host_all, host_groups))
        #         with ui.column().classes("w-full self-center").bind_visibility_from(host_groups, "value"):
        #             #searchbar = sayt(r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\Webui\csv's\lookup.csv")
        #             with ui.row().classes("w-full asolute-center self-center"):
        #                 ui.button("Submit", on_click= callfunc_place_submitted).classes("self-center").props("outline")
        #                 if system() == "Windows":
        #                     await sayt(r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\Webui\csv's\lookup.csv")
        #                 else:
        #                     await sayt(r"/home/nick/Ansible-Website/Webui/csv's/lookup.csv")
        #                 global searchresults_column_hostgroups
        #             searchresults_column_hostgroups = ui.column().classes("w-full items-center")
                        
        #         with ui.column().classes("w-full self-center").bind_visibility_from(host_individual, "value"):
        #             with ui.row().classes("w-full asolute-center self-center"):
        #                 ui.button("Submit", on_click=callfunc_place_submitted_copy).classes("center self-center").props("outline")
        #                 if system() == "Windows":
        #                     await sayt_copy(r"C:\Users\npodewils\Desktop\p\C.D.Buettner\Ansible-Website\Webui\csv's\lookup.csv")
        #                 else:
        #                     await sayt_copy(r"/home/nick/Ansible-Website/Webui/csv's/lookup.csv")
        #                 global searchresults_column_hostindividual
        #             searchresults_column_hostindividual = ui.column().classes("w-full items-center")
    
    
    

ui.run()

from nicegui import ui
def hallo(*args):
    print(args)

with ui.card() :
    ui.label("1")
    with ui.card() :
        ui.label("2")
        with ui.card() :
            ui.label("3")
            with ui.card() :
                ui.label("4")
                button = ui.button("add childs", on_click=lambda: print(button.parent_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.parent.default_slot.children.append(ui.label("hello"))))
    ui.label("1")
    with ui.card() :
        ui.label("2")
        with ui.card() :
            ui.label("3")
            with ui.card() as card:
                ui.label("4")
                card.on(type="click", handler=hallo)
ui.run()
from nicegui import ui




with ui.card() as card:
    with card.add_slot("childs"):
        with ui.row():
            ui.label('first')
            ui.label('first')
            ui.label('first')
            ui.label('first')
            ui.label('first')
            ui.label('first')
            ui.label('first')
            ui.label('first')
            ui.label('first')
            ui.label('first')
            ui.label('first')


with card:
    ui.label('second')
    card.default_slot.children.insert(len( card.default_slot.children), card.default_slot.children.pop())
    






ui.run()
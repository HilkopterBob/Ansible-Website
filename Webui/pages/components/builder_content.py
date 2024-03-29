from __future__ import annotations
from typing import Optional
from nicegui import ui

global Elements
global Playbook
class Column(ui.column):

    def __init__(self, name: str) -> None:
        super().__init__()
        with self.classes('p-4 rounded shadow').style("margin: 1px 0 0 1px; box-shadow: 0 0 0 1px #03DAC5;"):
            ui.label(name).classes('text-bold')
        self.name = name
        self.on('dragover.prevent', self.highlight)
        self.on('dragleave', self.unhighlight)
        self.on('drop', self.move_card)

    def highlight(self) -> None:
        pass # not needed 

    def unhighlight(self) -> None:
        pass # not needed

    def move_card(self) -> None:
        print(self.id)
        children = Playbook.default_slot.children
        print(children)
        for x in children:
            print(x.id)
        print("--------------------------------")
        if self.id not in Elements._collect_descendant_ids():

            with self:
                """
                The moved element is only created if it is not dropped in Elements, or in a child of Elements. 
                """
                return Card(Card.dragged.text, Card.dragged.child_container, Card.dragged.extendable)
                


        self.unhighlight()
        if Card.dragged.parent_slot.parent.name != "Elements":
            Card.dragged.parent_slot.parent.remove(Card.dragged)
            """
            only if the parent is not the elements card, the drag-n-drop element is removed
            """


class Card(ui.card):
    dragged: Optional[Card] = None

    def __init__(self, text: str, child_container: bool = False, extendable: bool = False) -> None:
        super().__init__()
        self.text = text
        self.name = text
        self.child_container = child_container
        self.extendable = extendable

        with self.props('draggable').classes('w-full cursor-pointer'):
            ui.label(self.text)
        self.on('dragstart', self.handle_dragstart)

        if self.child_container == True:
            with self:
                global row
                if self.extendable:
                    with ui.row():
                        ui.button("", on_click=lambda: self.add_child_container(row)).props("icon=add outline")
                        ui.button("", on_click=lambda: self.remove_child_container(row)).props("icon=remove outline")
                with ui.row() as _row:
                    row = _row
                self.add_child_container(row)


    def handle_dragstart(self) -> None:
        Card.dragged = self

    def add_child_container(self, parrent):
        with parrent:
            Column("added Child container")
    
    def remove_child_container(self, parrent):
        try:
            parrent.remove(-1)
        except IndexError:
            pass

async def content():
    global Elements
    global Playbook
    with ui.element("div").classes("w-full") as div:
        with ui.row().classes("w-full items-center justify-between") as Playbook:
            with Column('Current Playbook').classes("w-3/5"):
                Card('Work in Progress...')
            with Column('Elements').classes("w-1/5") as Elements:
                Card('Work in Progress...')
                Card('Work in Progress...with child slot, non extendable', child_container=True)
                Card('Work in Progress...with child slot, extendable', child_container=True, extendable=True)
    return div





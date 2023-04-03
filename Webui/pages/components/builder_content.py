from __future__ import annotations
from typing import Optional
from nicegui import ui


class Column(ui.column):

    def __init__(self, name: str) -> None:
        super().__init__()
        with self.classes('bg-gray-900 w-48 p-4 rounded shadow'):
            ui.label(name).classes('text-bold')
        self.on('dragover.prevent', self.highlight)
        self.on('dragleave', self.unhighlight)
        self.on('drop', self.move_card)

    def highlight(self) -> None:
        # self.classes(add='bg-gray-400')
        pass

    def unhighlight(self) -> None:
        # self.classes(remove='bg-gray-400')
        pass

    def move_card(self) -> None:
        self.unhighlight()
        Card.dragged.parent_slot.parent.remove(Card.dragged)
        with self:
            Card(Card.dragged.text)


class Card(ui.card):
    dragged: Optional[Card] = None

    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text
        with self.props('draggable').classes('w-full cursor-pointer'):
            ui.label(self.text)
        self.on('dragstart', self.handle_dragstart)

    def handle_dragstart(self) -> None:
        Card.dragged = self



async def content():
    with ui.row().classes("w-full"):
        with Column('Current Playbook').classes("w-75"):
            Card('Work in Progress...')
            Card('Work in Progress...')
            Card('Work in Progress...')
        with Column('Elements').classes("w-25"):
            Card('Work in Progress...')









from nicegui import ui, app
from fastapi import Request
from contextlib import contextmanager
from starlette.middleware.sessions import SessionMiddleware
from typing import Dict
from fastapi.responses import RedirectResponse
import asyncio

global clicks
clicks = 0

async def notify():
    global clicks
    ui.notify("clicked", type="positive")
    clicks = clicks + 1


with ui.dialog() as dialog, ui.card():
    ui.label("Trag den namen ein, unter dem dein highscore angezeigt werden soll:")
    name_field = ui.input()
    ui.button("Enter", on_click=lambda: dialog.submit(name_field.value))


async def save_scroe():
    scores = open("scores.txt","a")
    name = await dialog()
    scores.writelines(f"name: {name} got {clicks} clicks!")
    ui.open("/")

async def start_timer():
    timer = ui.circular_progress(max=15, min=0)
    i = 15
    clicker = ui.button("click", on_click=notify)
    while i >= 0:
        timer.set_value(i)
        await asyncio.sleep(1)
        i-=1
    timer.classes("hidden")
    clicker.classes("hidden")
    ui.label(f"Du hast {clicks} clicks erreicht!")
    save_button = ui.button("Um deinen highscore zu speicher, click mich", on_click=save_scroe)
    ui.button("restart", on_click=lambda: ui.open("/"))





@ui.page('/')
async def index_page(request: Request) -> None:
    return await content(request)

async def content(request: Request) -> None:
    ui.button("start clicker", on_click=lambda: dialog.open())




ui.run()
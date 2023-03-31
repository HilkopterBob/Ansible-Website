"""search as you type Searchbar component
"""
import asyncio
from typing import Optional
import csv
from nicegui import events, ui

checked_results = []
running_query: Optional[asyncio.Task] = None
async def search_in_csv(search_term):
    response = []
    with open(file_path, 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for _row in reader:
            for field in _row:
                if str(search_term) in str(field):
                    response.append(str(_row))
    return response

async def search(e: events.ValueChangeEventArguments) -> None:
    global running_query
    if running_query:
        running_query.cancel() 
    search_field.classes('mt-2', remove='mt-24') 
    results_container.clear()
    if e.value == "":
        clear_checked_results()
    running_query = asyncio.create_task(search_in_csv(e.value))
    response = await running_query
    for index, item in enumerate(response):
        if item == "":
            response.pop(index)
    if response != []:
        with results_container:  
            with ui.element("div").classes('w-full items-center self-center') as results_sec_container:
                for item in response:  # iterate over the response data of the api
                    with ui.row().classes('w-full items-center self-center') as Row:
                        checkbox = ui.checkbox(text=item, on_change=check).classes('self-center')
    running_query = None

# create a search field which is initially focused and leaves space at the top
# fr fr falls das jemand ließt, dass was da unten los ist ist mir echt peinlich, 
# aber hauptsache ich hab nachher search as you type auf der page
def sayt (file):
    print()
    global checked_results
    global search_field
    global results
    global results_container
    global results_sec_container
    global file_path
    file_path = file
    search_field = ui.input(on_change=search) \
        .props('input-class="ml-3"') \
        .classes('w-96 self-center transition-all')
    results_container = ui.card().classes('w-full items-center').bind_visibility_from(search_field, "value")
    return checked_results

def get_checked_results():
    return checked_results

async def check(event: events.ValueChangeEventArguments):
    if event.sender.value == True:
        checked_results.append(event.sender.text)
    if event.sender.value == False:
        checked_results.remove(event.sender.text)

def clear_checked_results():
    global checked_results
    checked_results = []


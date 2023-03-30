"""search as you type Searchbar component
"""
import asyncio
from typing import Optional
import csv


from nicegui import events, ui
checked_results = []
def yield_search_result(checkbox_value):
    if checkbox_value == True:
        return True

running_query: Optional[asyncio.Task] = None
async def search_in_csv(search_term):
    response = []
    with open(file_path, 'rt') as f:
        reader = csv.reader(f, delimiter=',') # good point by @paco
        for row in reader:
            for field in row:
                if str(search_term) in str(field):
                    response.append(str(row))

    return response

async def search(e: events.ValueChangeEventArguments) -> None:
    '''Search for cocktails as you type.'''
    global running_query
    if running_query:
        running_query.cancel()  # cancel the previous query; happens when you type fast
    search_field.classes('mt-2', remove='mt-24')  # move the search field up
    results.clear()
    # store the http coroutine in a task so we can cancel it later if needed
    if e.value == "":
        pass
    running_query = asyncio.create_task(search_in_csv(e.value))
    response = await running_query
    for index, item in enumerate(response):
        if item == "":
            response.pop(index)
    if results != []:
        with results:  # enter the context of the the results row

            for item in response:  # iterate over the response data of the api
                with ui.row().classes('w-full items-center self-center'):
                    checkbox = ui.checkbox("", value=False).classes('self-center')
                    ui.label(item).classes('self-center')
                    checkbox.on_value_change(get_checked_results(checkbox.value, item))




    running_query = None


# create a search field which is initially focused and leaves space at the top
# fr fr falls das jemand ließt, dass was da unten los ist ist mir echt peinlich, 
# aber hauptsache ich hab nachher search as you type auf der page
def sayt (file):
    global checked_results
    global search_field
    global results
    global file_path
    file_path = file
    search_field = ui.input(on_change=search) \
        .props('autofocus item-center input-class="ml-3"') \
        .classes('w-96 self-center transition-all')
    results = ui.card().classes('w-full items-center').bind_visibility_from(search_field, "value")
    return checked_results


def get_checked_results(value, item):
    print("called")
    if value == True:
        checked_results.append(item)
    return checked_results






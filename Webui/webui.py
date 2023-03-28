from nicegui import ui

from pages import conf
from pages import login_page, landng_page, logout
ui.colors(primary=conf.primary_color)

ui.run(port=80, dark=True)
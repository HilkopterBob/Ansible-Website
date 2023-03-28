from nicegui import ui


from pages import login_page, landng_page, logout, admin_panel
ui.colors(primary="#BB86FC")

ui.run(port=80, dark=True)
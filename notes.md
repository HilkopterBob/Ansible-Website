





- session middleware aus landing.py (pages) in Utils modul auslagern  

- dinge zentrieren:
```
.classes('absolute-center items-center')
```

- spacing: .classes("w-10/12") (geht auch für h)  

- navbar:
   ```
    with ui.header().style("background-color: #1d1d1d").classes("items-center justify-between"):
        ui.label("büttnerlogo")
        ui.button(on_click=lambda: right_drawer.toggle()).props("icon=menu")
    
    
    
    ```


# shuld be done:

 - user settings implementieren

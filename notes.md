





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
 - add-hoc commands/bereich implementieren (mit unseren daten playbooks sofort ausführen, super ober mega schnell, vereinfachtes gui)
 - listitem innenleben ausgestalten (in der history muss unbedingt ein bericht ausgegeben werden)
 - schnittstellenanforderung ausarbeiten für listitem plays
 - formular für ticketsystem einrichten (usability/feadback)
 - Rubriken nach firmen
 - optionaler whitemode (mit Rot und weiß) irgh
 - man kann auf admin panel wechseln als normaler user
 - login screen aufhübschen mit zb. logo und Ansible automation hub uso
 - formatierung von suchergebnissen 


## new branch modularization

 - alles auf modularisierung und best practices umbauen
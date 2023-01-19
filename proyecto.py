import flet as ft



def main(page: ft.Page):
   
    vEquipos = ["Madrid", "Barsa", "Mogón","Villacarrillo"]
    vEquiposSelecionados = []
    
    menu = ft.Dropdown(width=100)

    for equipo in vEquipos:
        menu.options.append(ft.dropdown.Option(equipo))

    

    #ft.dropdown.Option("Red"),

    page.add(menu)





ft.app(target=main)
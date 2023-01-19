import flet as ft



def main(page: ft.Page):
   
    def cambiar_imagen(e):
        if (menu.value == "Madrid"):
            img.src = "Madrid.png"
            print("hola")
        elif (menu.value == "Barsa"):
            img.src = "Barsa.png"
        else:
            img.src = "SinImagen.png"
        page.update()




    vEquipos = ["Madrid", "Barsa", "Mogón","Villacarrillo"]
    vEquiposSelecionados = []
    
    menu = ft.Dropdown(hint_text="Selecciona un equipo",width=250, on_change=cambiar_imagen)

    for equipo in vEquipos:
        menu.options.append(ft.dropdown.Option(equipo))

    
    img = ft.Image(src=f"a")
    


    page.add(menu,img)





ft.app(target=main,assets_dir="imagenes")
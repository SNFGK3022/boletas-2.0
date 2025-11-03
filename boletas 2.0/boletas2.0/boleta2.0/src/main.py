import flet as ft


def main(page: ft.Page):
    page.title = "Boletas de calificasiones"
    page.bgcolor = "purple"
    page.window_width = 1600
    page.window_heiht = 600
    
    lista_alumnos = ft.Dropdown(
        width=300,
        label="Alumnos",
        options=[
            ft.dropdown.Option("Juan Manuel Martinez"),
            ft.dropdown.Option("Laija Mendez Carlos Daniel"),
            ft.dropdown.Option("Tapia Hernandez Jose Alejandro"),
            ft.dropdown.Option("Luz Paulina Nieto Manriquez"),
            ft.dropdown.Option("Juan Carlos Mendoza Rosas"),
        ],
    )
    
    esp = ft.Dropdown(
        width=200,
        label="Español",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )
    
    mat = ft.Dropdown(
        width=200,
        label="Matematicas",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )
    
    ing = ft.Dropdown(
        width=200,
        label="Ingles",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )
    
    info = ft.Dropdown(
        width=200,
        label="Informatica",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )
    
    hist = ft.Dropdown(
        width=200,
        label="Historia",
        options=[ft.dropdown.Option(str(i)) for i in range(10, 101, 10)]
    )
    
    label_promedio = ft.Text(value="", size=20, width=100, color="white")
    
    
    tabla_calificaciones = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Alumno")),
            ft.DataColumn(label=ft.Text("Español")),
            ft.DataColumn(label=ft.Text("Matematicas")),
            ft.DataColumn(label=ft.Text("Ingles")),
            ft.DataColumn(label=ft.Text("Informatica")),
            ft.DataColumn(label=ft.Text("Historia")),
            ft.DataColumn(label=ft.Text("Promedio")),
        ],
        rows=[]
    )
    
   
    mensaje_error = ft.Text(value="", color="red", size=16)
    
    def calcular_promedio(e):
       
        if not lista_alumnos.value:
            mensaje_error.value = "Por favor selecciona un alumno"
            page.update()
            return
            
       
        alumno_actual = lista_alumnos.value
        for fila in tabla_calificaciones.rows:
            if fila.cells[0].content.value == alumno_actual:
                mensaje_error.value = f"El alumno {alumno_actual} ya está en la tabla"
                page.update()
                return
        
        
        mensaje_error.value = ""  
        
        notas = [
            int(esp.value or 0),
            int(mat.value or 0),
            int(ing.value or 0),
            int(info.value or 0),
            int(hist.value or 0),
        ]
        promedio = sum(notas) / len(notas)
        label_promedio.value = f"{promedio:.2f}"
        
        nueva_fila = ft.DataRow(cells=[
            ft.DataCell(ft.Text(alumno_actual)),
            ft.DataCell(ft.Text(esp.value or "")),
            ft.DataCell(ft.Text(mat.value or "")),
            ft.DataCell(ft.Text(ing.value or "")),
            ft.DataCell(ft.Text(info.value or "")),
            ft.DataCell(ft.Text(hist.value or "")),
            ft.DataCell(ft.Text(f"{promedio:.2f}")),
        ])
        tabla_calificaciones.rows.append(nueva_fila)
        page.update()
    
    def borrar_todo(e):
        tabla_calificaciones.rows.clear()
        label_promedio.value = ""
        mensaje_error.value = ""  
        page.update()
        
    boton_calcular = ft.ElevatedButton(text="Calcular promedio", on_click=calcular_promedio)
    boton_borrar = ft.ElevatedButton(text="Borrar todo", on_click=borrar_todo, color="red")

    
    fila_dropdowns = ft.Row(
        [
            lista_alumnos,
            esp,
            mat,
            ing,
            info,
            hist,
            label_promedio
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )
    
    fila_boton = ft.Row(
        [boton_calcular, boton_borrar],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.add(
        ft.Column(
            [
                fila_dropdowns,
                mensaje_error,  
                fila_boton,
                tabla_calificaciones
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )
    
ft.app(target=main,view=ft.WEB_BROWSER)
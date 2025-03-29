import flet as ft  # type: ignore

def main(page: ft.Page):
    page.title = "Chat"
    page.vertical_alignment = "stretch" 

    # ListView para los mensajes con scroll automático
    messages = ft.ListView(expand=True, auto_scroll=True)

    # Variable para almacenar el nombre del usuario
    username = ""

    def on_message(msg):
        messages.controls.append(ft.Text(msg))
        messages.scroll_to(len(messages.controls) - 1)
        page.update()
    
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        nonlocal username
        if message.value.strip():
            # Se envía el mensaje usando el nombre almacenado
            page.pubsub.send_all(f"{username}: {message.value}")
            message.value = ""
            page.update()
    
    def set_username(e):
        nonlocal username
        if username_field.value.strip():
            username = username_field.value
            username_dialog.open = False  
            page.update()

    # Diálogo para pedir el nombre una sola vez al inicio
    username_field = ft.TextField(hint_text="Tu Nombre")
    set_name_button = ft.ElevatedButton("Guardar", on_click=set_username)
    username_dialog = ft.AlertDialog(
        title=ft.Text("Ingresa tu nombre"),
        content=ft.Column([username_field]),
        actions=[set_name_button]
    )
    page.overlay.append(username_dialog)
    username_dialog.open = True
    page.update()
    
    # Control de entrada para el mensaje
    message = ft.TextField(hint_text="Tu Mensaje...", expand=True)
    send = ft.ElevatedButton("Enviar", on_click=send_click)
    
    input_controls = ft.Column(
        controls=[message, send],
        spacing=10
    )
    
    layout = ft.Column(
        controls=[
            ft.Container(
                content=messages,
                expand=True,
            ),
            input_controls
        ],
        expand=True
    )
    
    page.add(layout)

# Punto de entrada
ft.app(target=main, view=ft.AppView.WEB_BROWSER)

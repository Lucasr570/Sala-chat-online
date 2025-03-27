import flet as ft  # type: ignore

def main(page: ft.Page):
    page.title = "Chat"
    page.vertical_alignment = "stretch" 

    # Creamos un ListView para los mensajes con scroll automático
    messages = ft.ListView(expand=True, auto_scroll=True)
    
    def on_message(msg):
        messages.controls.append(ft.Text(msg))
        messages.scroll_to(len(messages.controls) - 1)
        page.update()
    
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        if message.value.strip():  # Evitamos enviar mensajes vacíos
            page.pubsub.send_all(f"{user.value}: {message.value}")
            message.value = ""
            page.update()
    
    # Definimos los controles de entrada
    user = ft.TextField(hint_text="Tu Nombre", width=150)
    message = ft.TextField(hint_text="Tu Mensaje...", expand=True)
    send = ft.ElevatedButton("Send", on_click=send_click)
    
    # Layout principal y la fila de entrada fija
    layout = ft.Column(
        controls=[
            ft.Container(
                content=messages,
                expand=True,
            ),
            ft.Row(controls=[user, message, send])
        ],
        expand=True
    )
    
    page.add(layout)

# Punto de entrada 
ft.app(target=main, view=ft.AppView.WEB_BROWSER)

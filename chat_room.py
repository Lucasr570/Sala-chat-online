import flet as ft

def main(page: ft.Page):
    page.title = "Chat"
    
    def on_message(msg):
        # Agregar el mensaje recibido a la columna
        messages.controls.append(ft.Text(msg))
        page.update()
        
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        # Enviar el mensaje con el formato "usuario: mensaje"
        page.pubsub.send_all(f"{user.value}: {message.value}")
        message.value = ""  # Limpiar campo de mensaje después de enviarlo
        page.update()
        
    messages = ft.Column()  # Aquí se agregarán los mensajes
    user = ft.TextField(hint_text="Tu Nombre", width=150)
    message = ft.TextField(hint_text="Tu Mensaje...", expand=True)
    send = ft.ElevatedButton("Send", on_click=send_click)
    
    # Añadir los controles de entrada y el botón al layout
    page.add(messages, ft.Row(controls=[user, message, send]))

# Iniciar la aplicación
ft.app(main, view=ft.AppView.WEB_BROWSER)
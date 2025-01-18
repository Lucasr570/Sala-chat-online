import flet as ft

def main(page: ft.Page):
    page.title = "Chat"
    
    def on_message(msg):
        messages.controls.append(ft.Text(msg))
        page.update()
    
    page.pubsub.subscribe(on_message)
    
    def send_click(e):
        page.pubsub.send_all(f"{user.value}: {message.value}")
        message.value = ""
        page.update()
    
    messages = ft.Column()
    user = ft.TextField(hint_text="Tu Nombre", width=150)
    message = ft.TextField(hint_text="Tu Mensaje...", expand=True)
    send = ft.ElevatedButton("Send", on_click=send_click)
    
    page.add(messages, ft.Row(controls=[user, message, send]))

# Este es el punto de entrada compatible con Vercel
ft.app(target=main, view=ft.AppView.WEB_BROWSER)

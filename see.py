import flet as ft

def main(page : ft.Page):

    def restar(self):
        numero = int(numberText.value)
        numero-=1
        numberText.value = str(numero)
        page.update()

    def sumar(self):
        numero = int(numberText.value)
        numero+=1
        numberText.value = str(numero)
        page.update()

    minusButton = ft.ElevatedButton(text="-", on_click=restar)
    plusButton = ft.ElevatedButton(text="+", on_click=sumar)
    numberText = ft.Text(value="0")
    filaPrincipal = ft.Row(controls=[minusButton, numberText,  plusButton])

    page.add(filaPrincipal)

ft.app(target=main)
import flet as ft

def main(page:ft.Page):

    def change(e):
        select.value = f"you've chosen the color: {options.value}"
        page.update()

    def addcolor(e):
        options.options.append(ft.dropdown.Option(userOption.value))
        messageadd.value = f"you've added the color: {userOption.value}"
        userOption.value = ""
        page.update()

    options = ft.Dropdown(hint_text="colors", width=200,on_change=change,
                          options=[
                            ft.dropdown.Option("blue"),
                            ft.dropdown.Option("green"),
                            ft.dropdown.Option("red"),
                        ])
    userOption = ft.TextField(hint_text="add a new color here: ")
    addoption = ft.ElevatedButton("add color", on_click=addcolor)
    messageadd = ft.Text("")

    addrowOption = ft.Row(controls=[userOption, addoption])


    select = ft.Text("")
    page.add(options,addoption,select, messageadd, addrowOption)

ft.app(target=main)
import flet as ft

def main(page: ft.Page):

    def addItem(e):
        shoppinglist.controls.append(ft.Text(putitem.value))
        page.update()

    def removeItem(e):
       shoppinglist.value
       for shoppinglist in shoppinglist.controls:
           if putitem.text == shoppinglist.value:
               shoppinglist.value
       page.update()

    putitem = ft.TextField(label="What would you like?")

    addbutton = ft.ElevatedButton(text="Add item", on_click=addItem)
    removebutton = ft.ElevatedButton(text="Remove item", on_click=removeItem)
    clearlist = ft.ElevatedButton(text="Clear List")
    shoppinglist = ft.Column()
    page.update()

    page.add(putitem, addbutton, removebutton, clearlist, shoppinglist)

ft.app(target=main)
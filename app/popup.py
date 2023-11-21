import flet as ft

def open_dlg():
    def close_dlg(self, e):
        self.dlg_modal.open = False
        self.update()
        
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    dlg_modal.open = True
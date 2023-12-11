import flet as ft
from board import Board
import event
import todo
from popup_color_item import PopupColorItem

def main(page: ft.Page):
    # 각 네비게이션 인덱스에 따라 메인 콘텐츠 변경 노출
    def changeMainContent(e):
        pageIdx = e.control.selected_index

        if (pageIdx == 0):
            nowPage = todo.render()
        elif (pageIdx == 1):
            nowPage = Board()
        else:
            nowPage = event.render()
        
        page.controls.clear()
        page.add(nowPage)
        page.add(ft.Row(
            controls=[floating_button1, floating_button2],
            alignment=ft.MainAxisAlignment.END,  # 하단 정렬
        ))

    # 실제 main 페이지 데이터 노출 영역
    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.TASK_ALT_ROUNDED, label="My Todo"),
            ft.NavigationDestination(
                icon=ft.icons.DASHBOARD_OUTLINED,
                selected_icon=ft.icons.DASHBOARD_SHARP,
                label="Board"
            ),
            ft.NavigationDestination(icon=ft.icons.CARD_GIFTCARD_ROUNDED, label="Event"),
            
        ],
        on_change=changeMainContent
    )

    # 가로 비율 480 고정
    page.window_width = "480"
    
    # 가운데 정렬
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # height 판별 후 자동 스크롤
    page.scroll = "AUTO"

    #left_nav = LeftNavigationMenu()
    dark_light_text = ft.Text("Light theme")

    floating_button1 = ft.FloatingActionButton(
        content=ft.IconButton(
                    icon=ft.icons.BRIGHTNESS_2_OUTLINED,
                    tooltip="Toggle brightness",
                    on_click=theme_changed
                ),
    )

    floating_button2 = ft.FloatingActionButton(
        content=ft.PopupMenuButton(
                    icon=ft.icons.COLOR_LENS_OUTLINED,
                    items=[
                        PopupColorItem(
                            color="deeppurple", name="Deep purple"
                        ),
                        PopupColorItem(color="indigo", name="Indigo"),
                        PopupColorItem(color="blue", name="Blue"),
                        PopupColorItem(color="teal", name="Teal"),
                        PopupColorItem(color="green", name="Green"),
                        PopupColorItem(color="yellow", name="Yellow"),
                        PopupColorItem(color="orange", name="Orange"),
                        PopupColorItem(
                            color="deeporange", name="Deep orange"
                        ),
                        PopupColorItem(color="pink", name="Pink"),
                    ],
                )     
    )

    page.add(todo.render())
    page.add(ft.Row(
        controls=[floating_button1, floating_button2],
        alignment=ft.MainAxisAlignment.END,  # 하단 정렬
    ))

def theme_changed(self):
    if self.page.theme_mode == ft.ThemeMode.LIGHT:
        self.page.theme_mode = ft.ThemeMode.DARK
    else:
        self.page.theme_mode = ft.ThemeMode.LIGHT
    self.page.update()

ft.app(
    target=main,
    assets_dir="assets"
)
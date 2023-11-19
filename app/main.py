import flet as ft
import board
import event


nowPage = "todo"


def main(page: ft.Page):
    global nowPage

    # 각 네비게이션 인덱스에 따라 메인 콘텐츠 변경 노출
    def changeMainContent(e):
        global nowPage

        pageIdx = e.control.selected_index

        if (pageIdx == 0):
            nowPage = ft.Text("todo")
        elif (pageIdx == 1):
            nowPage = ft.Text("friends")
        elif (pageIdx == 2):
            nowPage = board.render()
        else:
            nowPage = event.render()
        
        page.controls.clear()
        page.add(nowPage)

    # 실제 main 페이지 데이터 노출 영역
    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.TASK_ALT_ROUNDED, label="My Todo"),
            ft.NavigationDestination(icon=ft.icons.SOCIAL_DISTANCE_OUTLINED, label="Friends Todo"),
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
    # height 판별 후 자동 스크롤
    page.scroll = "AUTO"
    page.add(ft.Text('todo'))

ft.app(
    target=main,
    assets_dir="assets"
)
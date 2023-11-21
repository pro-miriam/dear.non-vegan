import flet as ft
import board
import event
import todo

def main(page: ft.Page):
    # 각 네비게이션 인덱스에 따라 메인 콘텐츠 변경 노출
    def changeMainContent(e):
        pageIdx = e.control.selected_index

        if (pageIdx == 0):
            nowPage = todo.render()
        elif (pageIdx == 1):
            nowPage = board.render()
        #elif (pageIdx == 2):
        #    nowPage = ft.Text("friends")
        else:
            nowPage = event.render()
        
        page.controls.clear()
        page.add(nowPage)

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
            #ft.NavigationDestination(icon=ft.icons.SOCIAL_DISTANCE_OUTLINED, label="Friends Todo"),
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

    #초기 화면 (투두리스트)
    # page.add(todo.render())
    page.add(todo.render())

ft.app(
    target=main,
    assets_dir="assets",
    #view=ft.AppView.WEB_BROWSER
)
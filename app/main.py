import flet as ft
from board import Board
import event
import todo

## 게시글 리스트 최초 로드 후 변수 저장 
boardList = [
    {
        'username': 'USER_01',
        'user_img': 'images/default_user.png',
        'content_img': 'images/sample_01.png',
        'content': '이렇게 맛있는 비건 음식이 있을 줄은 몰랐어요! 앞으로 자주 사먹을 것 같습니다 ㅎㅎ'
    },
    {
        'username': 'USER_02',
        'user_img': 'images/default_user.png',
        'content_img': 'images/sample_02.png',
        'content': '하루하루 미션을 클리어하는 재미가 있습니다. 그리 어려운 난이도의 퀘스트도 아니라서 스트레스 없이 즐길 수 있어 좋아요 하루하루 미션을 클리어하는 재미가 있습니다. 그리 어려운 난이도의 퀘스트도 아니라서 스트레스 없이 즐길 수 있어 좋아요 하루하루 미션을 클리어하는 재미가 있습니다. 그리 어려운 난이도의 퀘스트도 아니라서 스트레스 없이 즐길 수 있어 좋아요 하루하루 미션을 클리어하는 재미가 있습니다. 그리 어려운 난이도의 퀘스트도 아니라서 스트레스 없이 즐길 수 있어 좋아요',
        'tag': ['비비고', '만두', '김치만두']
    },
    {
        'username': 'USER_03',
        'user_img': 'images/default_user.png',
        'content_img': 'images/sample_03.png',
        'content': '몰랐던 비건 제품들을 이벤트를 통해 저렴하게 만나볼 수 있다는 점이 최고 장점이네요!!'
    },
    {
        'username': 'USER_04',
        'user_img': 'images/default_user.png',
        'content_img': 'images/sample_04.png',
        'content': '좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿! 좋아요 굿~ 좋아요 굿!'
    }
]

def main(page: ft.Page):
    # 각 네비게이션 인덱스에 따라 메인 콘텐츠 변경 노출
    def changeMainContent(e):
        pageIdx = e.control.selected_index

        if (pageIdx == 0):
            nowPage = todo.render()
        elif (pageIdx == 1):
            nowPage = Board(boardList)
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

    page.add(todo.render())

ft.app(
    target=main,
    assets_dir="assets"
)
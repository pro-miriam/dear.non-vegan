## BOARD PAGE ##

import flet as ft

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

showText = []

# 게시글 클릭 시 전체보기/간략히보기
def clickBoardContent(e):
    global showText

    nowIdx = e.control.data

    showText[nowIdx] = not showText[nowIdx]
    
    if (showText[nowIdx] is True):
        maxLine = None
        overflow = "auto"
        showImage = False
    else:
        maxLine = 2
        overflow = "ellipsis"
        showImage = True

    textContainer = e.control.content.controls[0]
    imageContainer = e.control.content.controls[1]
    
    # 정 안 되면 숨김 처리 후 이미지는 따로 클릭 시 모달창 띄우기 
    imageContainer.visible = showImage

    # 이미지 element를 column으로 바꿔서 한 줄 차지하게 만들기 시도 중
    # imageContainer = ft.Column(
    #     controls=[ft.Image(imageContainer.content)],
    #     width="100%"
    # )

    print(imageContainer)

    textContainer.content.max_lines = maxLine
    textContainer.content.overflow = overflow

    e.control.update()

# 게시판 리스트 html
def renderBoard(board, idx):
    global showText

    boardDom = [
        ft.Container(
            content=ft.Text(
                value=board['content'],
                max_lines=2,
                overflow="ellipsis"
            ),
            expand=4
        )
    ]

    if board['content_img'] != '':
        boardDom.append(
            ft.Container(
                content=ft.Image(
                    src=f"{board['content_img']}",
                    fit=ft.ImageFit.CONTAIN,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(10)
                ),
                expand=1
            )
        )

    mainDom = [
        ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.CircleAvatar(
                        content=ft.Icon(ft.icons.FACE)
                    ),
                    ft.Text(value=board['username'])
                ]
            ),
            alignment=ft.alignment.center_left,
            height=50,
            border_radius=ft.border_radius.only(5, 5, 0, 0),
            padding=10
        ),
        ft.Container(
            content=ft.Row(
                controls=boardDom,
                alignment="SPACE_BETWEEN",
                vertical_alignment="START"
            ),
            alignment=ft.alignment.top_left,
            height="auto",
            border_radius=ft.border_radius.only(0, 0, 5, 5),
            padding=20,
            data=idx,
            on_click=clickBoardContent,
            border=ft.border.only(bottom=ft.border.BorderSide(1, ft.colors.GREY_300))
        )
    ]

    # Column:: 컬럼(한줄 차지)
    return ft.Column(
        controls=mainDom,
        spacing=0
    )

def render():
    global boardList
    global showText

    pchild = []
    for idx, board in enumerate(boardList):
        showText.append(False)

        # 컬럼(한줄 차지)
        pchild.append(renderBoard(board, idx))

    return ft.Column(
        pchild
    )
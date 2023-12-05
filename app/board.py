## BOARD PAGE ##
import flet as ft

class Board(ft.UserControl):
    def __init__(self, contents):
        super().__init__()
        self.showText = []
        self.contents = contents
    
    # 게시글 클릭 시 전체보기/간략히보기
    def clickBoardContent(self, e):
        nowIdx = e.control.data

        self.showText[nowIdx] = not self.showText[nowIdx]
        
        if (self.showText[nowIdx] is True):
            maxLine = None
            overflow = "auto"
            showImage = False
        else:
            maxLine = 2
            overflow = "ellipsis"
            showImage = True

        textContainer = e.control.content.controls[0]
        imageContainer = e.control.content.controls[1]
        
        # 이미지는 따로 클릭 시 모달창 띄우기 
        # imageContainer.visible = showImage

        # 이미지 element를 column으로 바꿔서 한 줄 차지하게 만들기 시도 중
        # imageContainer = ft.Column(
        #     controls=[ft.Image(imageContainer.content)],
        #     width="100%"
        # )

        #print(imageContainer)
        # print(self.page)

        textContainer.content.max_lines = maxLine
        textContainer.content.overflow = overflow

        e.control.update()
    
    # 게시판 리스트 html
    def renderBoard(self, board, idx):
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
                on_click=self.clickBoardContent,
                border=ft.border.only(bottom=ft.border.BorderSide(1, ft.colors.GREY_300))
            )
        ]

        # Column:: 컬럼(한줄 차지)
        return ft.Column(
            controls=mainDom,
            spacing=0
        )

    def build(self):
        pchild = []
        for idx, board in enumerate(self.contents):
            self.showText.append(False)

            # 컬럼(한줄 차지)
            pchild.append(self.renderBoard(board, idx))

        return ft.Column(pchild)
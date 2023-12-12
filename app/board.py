## BOARD PAGE ##
import flet as ft
import util

class Board(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.showText = []
        self.contents = util.read_board_list()
    
    # 나의 탄소 나뭇잎 레벨에 따른 컬러 조회
    def getMyLevelColor(self, lev):
        myLev       = int(lev)-1
        levColors   = [
            ft.colors.BLACK,
            ft.colors.DEEP_PURPLE,
            ft.colors.INDIGO,
            ft.colors.PINK,
            ft.colors.DEEP_ORANGE,
            ft.colors.ORANGE,
            ft.colors.YELLOW,
            ft.colors.TEAL,
            ft.colors.BLUE,
            ft.colors.GREEN
        ]

        return levColors[myLev]
    
    # 게시글 클릭 시 전체보기/간략히보기
    def clickBoardContent(self, e):
        nowIdx = e.control.data
        textContainer = e.control.content

        self.showText[nowIdx] = not self.showText[nowIdx]
        
        if (self.showText[nowIdx] is True):
            maxLine = None
            overflow = "auto"
        else:
            maxLine = 2
            overflow = "ellipsis"

        textContainer.max_lines = maxLine
        textContainer.overflow = overflow

        e.control.update()
    
    # 게시글 이미지 클릭 시 모달 오픈
    def clickBoardImage(self, e):
        imageContainer = e.control.content

        imageModal = ft.AlertDialog(
            content=ft.Image(
                src=f"{imageContainer.src}",
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10)
            )
        )

        self.page.dialog = imageModal
        imageModal.open = True
        self.page.update()
    
    # 게시판 리스트 html
    def renderBoard(self, board, idx):
        myLev = int(board['user_level']) if 'user_level' in board.keys() else 1
        boardDom = [
            ft.Container(
                content=ft.Text(
                    value=board['content'],
                    max_lines=2,
                    overflow="ellipsis"
                ),
                expand=4,
                data=idx,
                on_click=self.clickBoardContent
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
                    expand=1,
                    on_click=self.clickBoardImage
                )
            )

        mainDom = [
            ft.Container(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Icon(
                            ft.icons.ENERGY_SAVINGS_LEAF,
                            color=self.getMyLevelColor(myLev),
                            tooltip=f"LEVEL {myLev}"
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
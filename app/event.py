## EVENT PAGE ##

import flet as ft

eventBanners = [
    {
        'imageUrl': 'images/banner_01.jpg',
        'hrefLink': 'https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000165738&trackingCd=Home_Middle_Banner_PROD'
    },
    {
        'imageUrl': 'images/banner_02.jpg',
        'hrefLink': 'https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=B000000167311'
    },
    {
        'imageUrl': 'images/banner_03.jpg',
        'hrefLink': 'https://shopping.interpark.com/product/productInfo.do?prdNo=10595383503'
    },
    {
        'imageUrl': 'images/banner_04.jpg',
        'hrefLink': 'https://www.kurly.com/goods/5060444'
    },
]   

def render():
    global eventBanners

    banners = []
    for banner in eventBanners:
        dom = ft.Container(
            content=ft.Image(
                src=f"{banner['imageUrl']}",
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10)
            ),
            alignment=ft.alignment.center_left,
            height="auto",
            padding=5,
            url=banner['hrefLink']
        )

        # 컬럼(한줄 차지)
        banners.append(dom)

    return ft.Column(
        banners
    )
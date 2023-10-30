import flet as ft
from flet import *
from youdate import Youdate

def main(page:Page):
    page.window_width = 500
    page.add(Youdate())
    page.update()


ft.app(target=main)
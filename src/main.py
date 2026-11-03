import asyncio
from googletrans import Translator
from flet import *
from gui import Gui


def main(page: Page):
    page.window.resizable = False
    page.window.width = 750
    page.window.height = 330
    page.title = "Mini Tranlator"
    page.spacing = 0
    page.padding = 0

    page.add(Gui(page).build())


app(main, view=AppView.FLET_APP_WEB)

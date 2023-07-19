import flet
from flet import Page,Text


def main(page:Page):
    t1= Text("This is a text")
    page.title = "Hello"
    page.add(t1)
    page.update()

flet.app(target=main,view=flet.WEB_BROWSER,web_renderer="html")
from flet import *
from args import args, args2


class Gui:
    def __init__(self, page):
        self.page: Page = page

        self.left_container: Container = Container(
            bgcolor='transparent',
            expand=True,

            content=Column(
                controls=[
                    Dropdown(
                        value='auto',
                        width=330,
                        border_color='#8c8c8c',
                        enable_filter=True,
                        border_radius=8,
                        # options=[DropdownOption(key=k, text=v)
                        #          for k, v in args.items()]
                    ),
                    Container(
                        bgcolor='transparent',
                        width=330,
                        expand=True,
                        padding=padding.only(left=5),
                        alignment=alignment.top_left,
                        content=TextField(
                            hint_text='Enter text',
                            hint_style=TextStyle(
                                color='#757575',
                            ),
                            bgcolor='transparent',
                            border_color='transparent',
                            cursor_height=28,
                            cursor_color='white',
                            text_size=27,
                            hover_color='transparent',
                            multiline=True,
                            selection_color='#3c0ab1',
                            text_style=TextStyle(color='#ffffff'),
                            on_change=self.show_X_clear
                        )
                    )
                ]
            )
        )

        self.right_container: Container = Container(
            bgcolor='transparent',
            expand=True,
            content=Column(
                controls=[
                    Dropdown(
                        value='en',
                        width=330,
                        border_color='#8c8c8c',
                        enable_filter=True,
                        border_radius=8,
                        max_menu_height=56,
                        #     options=[DropdownOption(key=k, text=v)
                        #              for k, v in args2.items()]
                    ),
                    Container(
                        bgcolor='#303134',
                        border_radius=10,
                        width=330,
                        expand=True,
                        padding=padding.only(left=5),
                        alignment=alignment.top_left,
                        content=TextField(
                            value='Translation',
                            read_only=True,
                            bgcolor='transparent',
                            border_color='transparent',
                            text_size=27,
                            hover_color='transparent',
                            multiline=True,
                            selection_color='#3c0ab1',
                            text_style=TextStyle(
                                color='#989bab'),
                        )
                    )
                ]
            )
        )

    def show_X_clear(self, e):
        textfield: TextField = self.left_container.content.controls[1].content
        container: Column = self.page.controls[0].content.controls[1].content

        def on_click(e):
            textfield.value = ''
            container.controls.pop(1)
            self.page.update()
            textfield.focus()

        if textfield.value != '':
            if len(container.controls) >= 2:
                return

            container.controls.append(
                IconButton(
                    icon=Icons.CLOSE,
                    on_click=on_click,
                    icon_color='white54',
                    tooltip='Clear',
                    style=ButtonStyle(
                        shape={
                            "": RoundedRectangleBorder(radius=7)
                        },
                        overlay_color={"": 'transparent'}
                    )
                )
            )
        else:
            container.controls.pop(1)

        self.page.update()

    def swap_names(self, e):
        leftname = self.left_container.content.controls[0].value
        rightname = self.right_container.content.controls[0].value
        swapname = leftname
        leftname = rightname
        rightname = swapname
        self.page.update()

    def build(self):
        return Container(
            expand=True,
            padding=15,
            content=Row(
                controls=[
                    self.left_container,
                    Container(
                        height=300,
                        width=40,
                        bgcolor='transparent',
                        alignment=alignment.top_center,
                        margin=margin.only(top=5),
                        content=Column(
                            controls=[
                                IconButton(
                                    icon=Icons.SWAP_HORIZ,
                                    icon_color='white54',
                                    style=ButtonStyle(
                                        shape={
                                            "": RoundedRectangleBorder(radius=7)
                                        },
                                        overlay_color={"": 'transparent'},
                                    ),
                                    on_click=self.swap_names
                                )
                            ]
                        )
                    ),
                    self.right_container
                ]
            ),
        )

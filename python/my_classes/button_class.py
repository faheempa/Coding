from tkinter import *


class Button_class:
    def __init__(
        self,
        window,
        x: int,
        y: int,
        text=" ",
        color="#36ffe1",
        command=True,
        size=20,
        font="comic sans",
    ) -> None:
        self.x = x
        self.y = y
        self.text = text
        self.window = window
        self.command = command
        self.size = size
        self.font = font
        self.btn = Button(
            window,
            text=self.text,
            command=self.command,
            font=(self.font, self.size),
            fg="black",
            bg=color,
            activeforeground="red",
            activebackground="white",
            height=1,
            width=2,
        )
        self.btn.grid(row=self.x, column=self.y)

    def set_text(self, txt: str):
        self.text = txt
        self.btn.config(text=self.text)
        self.window.update()

    def set_command(self, command):
        self.command = command

    def set_xy(self, x, y):
        self.x = x
        self.y = y
        self.btn.config(row=self.x, column=self.y)
        self.window.update()

    def set_color(
        self, bg="white", fg="black", active_bg="blue", active_fg="light green"
    ):
        self.btn.config(
            bg=bg, fg=fg, activebackground=active_bg, activeforeground=active_fg
        )
        self.window.update()

    def set_height_width(self, height=2, width=4):
        self.btn.config(height=height, width=width)
        self.window.update()

    def set_font_and_size(self, font="comic sans", size=20):
        self.size = size
        self.font = font
        self.btn.config(font=(self.font, self.size))
        self.window.update()

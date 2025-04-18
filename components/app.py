from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()

        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.geometry("600x400")
        self.minsize(500, 300)
        self.maxsize(700, 500)
        self.title(f"SE Interview Project")

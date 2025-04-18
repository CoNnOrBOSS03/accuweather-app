from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()

        # appearance settings
        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.geometry("600x400")
        self.minsize(500, 300)
        self.maxsize(700, 500)
        self.title(f"SE Interview Project")

        # widgets
        self.title_text = CTkTextbox(master=self, fg_color="transparent", wrap=WORD, font=(None, 32),
                                     activate_scrollbars=False)
        self.title_text.insert("0.0", "Accuweather Weather Tracker")
        self.title_text.configure(state="disabled")
        self.search_bar = CTkEntry(master=self,
                                   placeholder_text="Enter City Name")
        self.search_button = CTkButton(master=self,
                                       text="Search")

        # placing widgets
        self.title_text.pack()
        self.search_bar.pack()
        self.search_button.pack()
from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()

        # appearance settings
        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.geometry("700x400")
        self.minsize(700, 400)
        self.maxsize(700, 400)
        self.title(f"SE Interview Project")

        # widgets
        self.left_frame = CTkFrame(master=self, fg_color="transparent")
        self.left_frame.place(relx=0, rely=0, relheight=1, relwidth=0.5)

        self.title_text = CTkTextbox(master=self.left_frame, fg_color="transparent", wrap=WORD, font=(None, 32),
                                     activate_scrollbars=False)
        self.title_text.insert("0.0", "Accuweather Weather Tracker")
        self.title_text.configure(state="disabled")
        self.title_text.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.25)

        self.secondary_frame = CTkFrame(master=self.left_frame, fg_color="transparent")
        self.secondary_frame.place(relx=0, rely=0.3, relheight=0.7, relwidth=1)

        self.prompt_text = CTkTextbox(master=self.secondary_frame, fg_color="transparent", wrap=WORD, font=(None, 14),
                                     activate_scrollbars=False)
        self.prompt_text.insert("0.0", "Please enter a city name to display weather conditions.")
        self.prompt_text.configure(state="disabled")
        self.search_bar = CTkEntry(master=self.secondary_frame,
                                   placeholder_text="Enter City Name")
        self.search_button = CTkButton(master=self.secondary_frame,
                                       text="Search")
        self.error_label = CTkLabel(master=self.secondary_frame, text="ERROR: Test error message. blebleblebble")

        self.right_frame = CTkFrame(master=self, corner_radius=0)
        self.right_frame.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)

        # placing widgets
        self.prompt_text.place(relx=0.15, rely=0.1, relheight=0.2, relwidth=.7)
        self.search_bar.place(relx=0.1, rely=0.35, relheight=0.1, relwidth=0.4)
        self.search_button.place(relx=0.6, rely=0.35, relheight=0.1, relwidth=0.3)
        self.error_label.place(relx=0.10, rely=0.6, relheight=0.2, relwidth=.8)
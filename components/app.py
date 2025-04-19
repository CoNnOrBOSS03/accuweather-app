import logging
from customtkinter import *
from api.accuweather_client import AccuWeatherClient
from components.weather_display import WeatherDisplay


class App(CTk):
    def __init__(self, api_key):
        super().__init__()

        # appearance settings
        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.geometry("700x400")
        self.minsize(700, 400)
        self.maxsize(700, 400)
        self.title(f"SE Interview Project - Connor Verra")

        # widgets
        self.leftFrame = CTkFrame(master=self, fg_color="transparent")
        self.leftFrame.place(relx=0, rely=0, relheight=1, relwidth=0.5)

        self.titleTextBox = CTkTextbox(master=self.leftFrame, fg_color="transparent", wrap=WORD, font=(None, 32),
                                       activate_scrollbars=False)
        self.titleTextBox.insert("0.0", "Accuweather Weather Tracker")
        self.titleTextBox.configure(state="disabled")
        self.titleTextBox.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.25)

        self.secondaryFrame = CTkFrame(master=self.leftFrame, fg_color="transparent")
        self.secondaryFrame.place(relx=0, rely=0.3, relheight=0.7, relwidth=1)

        self.promptTextBox = CTkTextbox(master=self.secondaryFrame, fg_color="transparent", wrap=WORD, font=(None, 14),
                                        activate_scrollbars=False)
        self.promptTextBox.insert("0.0", "Please enter a city name to display weather conditions.")
        self.promptTextBox.configure(state="disabled")
        self.searchBarEntry = CTkEntry(master=self.secondaryFrame,
                                       placeholder_text="Enter City Name")
        self.searchButton = CTkButton(master=self.secondaryFrame,
                                      text="Search",
                                      command=self.search_button_callback)
        self.errorLabel = CTkLabel(master=self.secondaryFrame, text="")

        self.rightFrame = CTkFrame(master=self, corner_radius=0)
        self.rightFrame.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)

        self.weatherDisplay = WeatherDisplay(master=self.rightFrame, api_key=api_key)
        self.weatherDisplay.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.8)
        self.toggleUnitsButton = CTkButton(master=self.rightFrame, text="Toggle Units",
                                           command=self.weatherDisplay.toggle_units)
        self.toggleUnitsButton.place(relx=0.05, rely=0.88, relwidth=0.9, relheight=0.07)

        # placing widgets
        self.promptTextBox.place(relx=0.15, rely=0.1, relheight=0.2, relwidth=.7)
        self.searchBarEntry.place(relx=0.1, rely=0.35, relheight=0.1, relwidth=0.4)
        self.searchButton.place(relx=0.6, rely=0.35, relheight=0.1, relwidth=0.3)
        self.errorLabel.place(relx=0.10, rely=0.6, relheight=0.2, relwidth=.8)

    def search_button_callback(self):
        # check to make sure search bar is not empty
        city_name = self.searchBarEntry.get()
        if city_name == "":
            self.set_error_text("Please enter a city name!")
            return
        try:
            self.weatherDisplay.set_display(city_name)
        except ValueError as e:
            self.set_error_text("City not found: please try again!")
            logging.error(str(e))
        except Exception as e:
            self.set_error_text("A miscellaneous error occurred.")
            logging.error(str(e))

    def set_error_text(self, text: str):
        self.errorLabel.configure(text=text)
        self.errorLabel.after(3000, lambda: self.errorLabel.configure(text=""))

    def toggle_units(self):
        pass

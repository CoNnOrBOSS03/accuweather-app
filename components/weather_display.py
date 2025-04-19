from customtkinter import *
from api.accuweather_client import AccuWeatherClient


class WeatherDisplay(CTkScrollableFrame):

    class ConditionsInfoCard(CTkFrame):
        def __init__(self, condition_name):

    def __init__(self, master, api_key):
        super().__init__(master=master, label_text="Current Conditions", fg_color="transparent")
        self.client: AccuWeatherClient = AccuWeatherClient(api_key=api_key)


    def configure_client(self, city_name: str):
        try:
            self.client.set_conditions_from_city(city_name)
            print(self.client.get_result("WeatherText"))

            # TODO: add condition info
        except ValueError:
            raise
        except Exception:
            raise

    def set
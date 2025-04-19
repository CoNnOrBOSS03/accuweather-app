from customtkinter import *
from api.accuweather_client import AccuWeatherClient

DISPLAYED_CONDITIONS = {
    "WeatherText": "Conditions",
    "HasPrecipitation": "Currently Raining",
    "Precip1hr": "Hourly Rainfall",
    "Temperature": "Temperature",
    "RelativeHumidity": "Humidity",
    "UVIndex": "UV Index"
}


class WeatherDisplay(CTkScrollableFrame):
    class ConditionInfoCard(CTkFrame):
        def __init__(self, master, condition_name, condition_value_dict):
            super().__init__(master=master, height=35)

            self.units = "imperial"

            self.condition_value_dict = condition_value_dict
            self.condition_value = self.clean_condition_value()

            self.conditionNameLabel = CTkLabel(master=self, text=f"{condition_name}: ")
            self.conditionValueLabel = CTkLabel(master=self, text=self.condition_value)

            self.conditionNameLabel.place(relx=0.05, rely=0.1, relwidth=0.5, relheight=0.8)
            self.conditionValueLabel.place(relx=0.6, rely=0.1, relwidth=0.35, relheight=0.8)

        def toggle_units(self):
            if self.condition_value_dict.get("dual-unit"):
                if self.units == "imperial":
                    self.units = "metric"
                else:
                    self.units = "imperial"
                self.conditionValueLabel.configure(text=self.clean_condition_value())

        def clean_condition_value(self):
            # handling data with metric/imperial units - should be expanded on to handle all accuweather data
            if self.condition_value_dict.get("dual-unit") is False:
                condition_value = self.condition_value_dict.get('value')
                if isinstance(condition_value, bool):
                    condition_value = self.handle_boolean(condition_value)
            else:
                condition_value = self.condition_value_dict.get(self.units)
            return condition_value

        def handle_boolean(self, bool_val: bool):
            if bool_val:
                return "Yes"
            return "No"

    def __init__(self, master, api_key):
        super().__init__(master=master, label_text="Current Conditions")
        self.client: AccuWeatherClient = AccuWeatherClient(api_key=api_key)
        self.conditionInfoCards = []

    def set_display(self, city_name: str):
        try:
            self.client.set_conditions_from_city(city_name)
            self.configure(label_text=f"Current Conditions for {city_name}")

            self._clear_conditions()
            for key, label in DISPLAYED_CONDITIONS.items():
                condition_value_dict = self.client.get_result(key)
                self.conditionInfoCards.append(
                    WeatherDisplay.ConditionInfoCard(
                        master=self,
                        condition_name=label,
                        condition_value_dict=condition_value_dict
                    )
                )
            self._display_conditions()

        except ValueError:
            raise
        except Exception:
            raise

    def _display_conditions(self):
        for card in self.conditionInfoCards:
            card: WeatherDisplay.ConditionInfoCard
            card.pack(padx=5, pady=1, fill=X, expand=False)

    def _toggle_units(self):
        for card in self.conditionInfoCards:
            card: WeatherDisplay.ConditionInfoCard
            card.toggle_units()

    def _clear_conditions(self):
        self.conditionInfoCards.clear()
        for card in self.winfo_children():
            card.destroy()

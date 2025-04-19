import json
import urllib.request
import urllib.error
import urllib.parse
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Change to INFO or WARNING to reduce verbosity
    format='[%(levelname)s] %(message)s'
)


class AccuWeatherClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://dataservice.accuweather.com"
        self.conditions = None

    def set_conditions_from_city(self, city: str):
        try:
            location_key = self._get_location_key(city)
            curr_conditions = self._get_current_conditions(location_key)
            self.conditions = curr_conditions
        except ValueError:
            raise
        except Exception:
            raise

    def get_result(self, result_name):
        if self.conditions is None:  # if accessed before location set
            return ""
        else:
            value = self.conditions[0].get(result_name)
            # handle metric/imperial units
            if self._in_units(value):
                return self._get_pretty_units(value)
            if value is None:
                return "Value Not Found"
            return {
                "dual-unit": False,
                "value": value
            }

    def _in_units(self, conditions_val):  # checks if given value has measurement units
        return isinstance(conditions_val, dict) and "Metric" in conditions_val and "Imperial" in conditions_val

    def _get_pretty_units(self, conditions_val):  # formats measurement units for display
        return {
            "dual-unit": True,
            "metric": f"{conditions_val['Metric']['Value']} {conditions_val['Metric']['Unit']}",
            "imperial": f"{conditions_val['Imperial']['Value']} {conditions_val['Imperial']['Unit']}"
        }

    def _get_data(self, url: str):  # generalizes api requests, passes errors up
        try:
            # print(f"Requesting URL: {url}")
            with urllib.request.urlopen(url) as response:
                if response.status != 200:
                    raise Exception(f"Accuweather API responded with status code {response.status}")
                data = json.loads(response.read().decode())
                if not data:
                    raise ValueError(f"No valid data returned: check input")
                return data
        except urllib.error.HTTPError as e:
            raise Exception(f"HTTP error occurred: {e.code} - {e.reason}")
        except urllib.error.URLError as e:
            raise Exception(f"URL error occurred: {e.reason}")
        except ValueError as e:
            raise ValueError(f"Value error occurred while parsing response: {str(e)}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

    def _get_location_key(self, city: str):
        encoded_city = urllib.parse.quote(city)
        url = f"{self.base_url}/locations/v1/cities/search?apikey={self.api_key}&q={encoded_city}"
        try:
            data = self._get_data(url)
            location_key = data[0]["Key"]
            return location_key
        except ValueError:
            raise ValueError(f"City {city} not found in Accuweather API")
        except Exception as e:
            raise Exception(f"An error occurred while getting the location key: {e}")

    def _get_current_conditions(self, location_key):
        url = f"{self.base_url}/currentconditions/v1/{location_key}?apikey={self.api_key}&details=true"
        try:
            data = self._get_data(url)
            return data
        except ValueError:
            raise
        except Exception:
            raise

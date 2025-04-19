import unittest
from api.accuweather_client import AccuWeatherClient
from config import ACCUWEATHER_API_KEY

class TestAccuWeatherClientMethods(unittest.TestCase):

    def test_get_location_key_valid(self):
        client = AccuWeatherClient(ACCUWEATHER_API_KEY)
        self.assertEqual(client._get_location_key("Tampa"), '347937')

    def test_get_temperature_invalid_city(self):
        client = AccuWeatherClient(ACCUWEATHER_API_KEY)
        with self.assertRaises(ValueError) as context:
            client._get_location_key("blebleblubleblu")
        self.assertEqual(str(context.exception), "City blebleblubleblu not found in Accuweather API")


if __name__ == '__main__':
    unittest.main()

from pyowm import OWM
import datetime

class WeatherAPI:
	def __init__(self, city):
		self.city = city
		self.owm = OWM("1ec584803deffede068b569491d027ef")
		self.mgr = self.owm.weather_manager()
		self.observation = self.mgr.weather_at_place(city)
		self.data = self.observation.weather

	def get_forecast(self):
		data = self.data
		self.forecast = {
			'date': datetime.datetime.fromtimestamp(int(data.reference_time())).strftime('%d'),
			'temperature': data.temperature(unit='fahrenheit')['temp'],
			'temp_max': data.temperature(unit='fahrenheit')['temp_max'],
			'temp_min': data.temperature(unit='fahrenheit')['temp_min'],
			'feels_like': data.temperature(unit='fahrenheit')['feels_like'],
			'humidity': data.humidity,
			'pressure': data.pressure['press'],
			'wind': data.wnd['speed'],
			'sunset': datetime.datetime.fromtimestamp(int(data.sunset_time())).strftime('%H:%M:%S'),
			'sunrise': datetime.datetime.fromtimestamp(int(data.sunrise_time())).strftime('%H:%M:%S')
			}
		return self.forecast

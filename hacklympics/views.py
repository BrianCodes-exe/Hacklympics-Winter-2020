from hacklympics import app
from flask import render_template, request, redirect
from pyowm import OWM
import datetime

class WeatherAPI:
	def __init__(self, city):
		self.city = city
		self.owm = OWM("1ec584803deffede068b569491d027ef")
		self.mgr = self.owm.weather_manager()
		self.observation = self.mgr.weather_at_place(city)
		self.city_ob = self.observation.to_dict()
		self.coordinates = self.city_ob['location']['coordinates']
		self.lat, self.lon = self.coordinates['lat'], self.coordinates['lon']
		self.city_info = self.mgr.forecast_at_place(city, '3h')

	def get_forecast(self):
		self.hours = [{}]
		self.call = self.mgr.one_call(self.lat, self.lon)
		self.hourly_forecast = self.call.forecast_hourly

		self.forecast = []

		for data in self.hourly_forecast:
			d = {
			'date': datetime.datetime.fromtimestamp(int(data.reference_time())).strftime('%d'),
			'hour': datetime.datetime.fromtimestamp(int(data.reference_time())).strftime('%H'),
			'temperature': data.temperature(unit='fahrenheit')['temp'],
			'feels_like': data.temperature(unit='fahrenheit')['feels_like'],
			'humidity': data.humidity,
			'pressure': data.pressure['press'],
			'wind': data.wnd['speed']
			}
			self.forecast.append(d)
		return self.forecast

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['post', 'get'])
def getCommand():
	user_input = request.form.get('command')
	if '/weather' in user_input:
		if ' ' in user_input:
			command = '/weather'
			city = user_input[9:]
			wapi = WeatherAPI(city)
			forecast = wapi.get_forecast()
			showData = True
			return render_template('index.html', command=command, forecast=forecast, showData=showData)
		elif user_input == '/weather':
			command = 'no city'

			return render_template('index.html', command=command)
	else:
		command = 'error'

		return render_template('index.html', command=command)

	

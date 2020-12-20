from hacklympics import app
from hacklympics.pyclass.WeatherAPI import WeatherAPI
from hacklympics.pyclass.NewsAPI import NewsAPI
from flask import render_template, request, redirect, url_for
import os
import time

os.environ["TZ"] = 	"America/Los_Angeles"
time.tzset()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['post', 'get'])
def getCommand():
	user_input = request.form.get('command')

	# Command for /weather
	if '/weather' in user_input:
		if ' ' in user_input:
			command = '/weather'
			city = user_input[9:]
			try:
				wapi = WeatherAPI(city)
				forecast = wapi.get_forecast()
				return render_template('index.html', command=command, forecast=forecast, city=city.title())
			except:
				command="cityDNE"
				return render_template('index.html', command=command, city=city.title())
		elif user_input == '/weather':
			command = 'no city'
			return render_template('index.html', command=command)

	# Command for /news
	if '/news' in user_input:
		command = '/news'
		if ' ' in user_input:
			keyword = user_input[6:]
			try:
				newsapi = NewsAPI(keyword)
				articles = newsapi.get_articles()
				return render_template('index.html', command=command, articles=articles, keyword=keyword)
			except:
				command = 'None Found'
				articles = None
				return render_template('index.html', command=command, keyword=keyword)

		elif user_input == '/news':
			newsapi = NewsAPI()
			articles = newsapi.get_top_headlines()
			showData = True
			return render_template('index.html', command=command, articles=articles, showData=showData)

	# Invalid command
	else:
		command = 'error'

		return render_template('index.html', command=command)
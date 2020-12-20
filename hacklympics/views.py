from hacklympics import app
from hacklympics.pyclass.WeatherAPI import WeatherAPI
from hacklympics.pyclass.NewsAPI import NewsAPI
from flask import render_template, request, redirect, url_for
import datetime


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
				showData = True
				return render_template('index.html', command=command, forecast=forecast, showData=showData)
			except:
				command='cityDNE'
				return render_template('index.html', command=command)
		elif user_input == '/weather':
			command = 'no city'
			return render_template('index.html', command=command)
	
	# Command for /news
	if '/news' in user_input:
		command = '/news'
		if ' ' in user_input:
			keyword = user_input[6:]
			newsapi = NewsAPI(keyword)
			articles = newsapi.get_articles()

			if articles == 'None Found':
				command=articles
				showData = False
			else:
				showData = True

			return render_template('index.html', command=command, articles=articles, keyword=keyword, showData=showData)

		elif user_input == '/news':
			newsapi = NewsAPI()
			articles = newsapi.get_top_headlines()
			showData = True
			return render_template('index.html', command=command, articles=articles, showData=showData)

	# Invalid command
	else:
		command = 'error'

		return render_template('index.html', command=command)

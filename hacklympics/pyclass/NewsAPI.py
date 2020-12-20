from newsapi import NewsApiClient
import config

class NewsAPI:

	def __init__(self, keyword=""):
		self.newsapi = NewsApiClient(api_key=NEWSAPI)
		self.keyword = keyword
		self.valid_sources = {}	
		self.get_valid_sources()

	def get_valid_sources(self):
		sources = self.newsapi.get_sources()

		for source in sources['sources']:
			self.valid_sources[source['name'].lower()] = source['id']

	def is_valid_source(self, source):
		return source in self.valid_sources

	def get_top_headlines(self):
		top_5 = []
		top_headlines = self.newsapi.get_top_headlines()
		for index in range(0, 20, 4):
			top_5.append(top_headlines['articles'][index])
		return top_5

	def get_articles(self):
		articles = self.newsapi.get_everything(qintitle=self.keyword)
		a = []
		for index in range(0, min(5, articles['totalResults'])):
			a.append(articles['articles'][index])

		if len(a) < 5:
			all_articles = self.newsapi.get_everything(q=self.keyword)
			if all_articles['totalResults'] + len(a) >= 5:
				for index in range(len(a), 5):
					a.append(all_articles['articles'][index])

		if len(a) > 0:
			return a
		else:
			return 'None Found' 

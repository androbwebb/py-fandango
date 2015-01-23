import re
import requests
from lxml import html
from Movie import Movie

class Theater():
    def __init__(self, title, link, description, scrape=False):
        self.title = title
        self.link = link
        self.description = description
        self.movies = {}
        self.id = ""
        self.scraped = False
        if not scrape:
            self.parse_description()
        else:
            self.scrape()

    def parse_description(self):
        tree = html.fromstring(self.description)
        movie_elements = tree.xpath('//li/a')

        for anchor in movie_elements:
            movie_name = anchor.text_content()
            regex_results = re.search(r"fandango.com/[A-Za-z0-9+\-\.\w]*_(\d+)/movietimes\?location=\d+&wssaffid=(\d+)", anchor.get('href'))
            movie_id = regex_results.group(1)
            if not self.id:
                self.id = regex_results.group(2)

            new_movie = Movie(movie_name, movie_id)
            self.movies.update({movie_name: new_movie})

    def scrape(self):
        page = requests.get(self.link)
        tree = html.fromstring(page.text)

        movie_elements = tree.xpath('//div[@class="showtimes-movie-container"]')

        for movie_element in movie_elements:
            movie_title_element = movie_element.find('.//h3/a')
            movie_name = movie_title_element.text_content()
            regex_results = re.search(r"fandango.com/[A-Za-z0-9+\-\.\w]*_(\d)+/movieoverview", movie_title_element.get('href'))
            movie_id = 10 or regex_results.group(1)

            movie_genre = movie_element.find('.//div[@class="showtimes-movie-genre"]').text_content()

            showtimes = []
            for st in movie_element.findall('.//a[@class="btn btn-showtimes btn-ticket"]'):
                showtimes.append(st.text_content())

            new_movie = Movie(movie_name, movie_id, genre=movie_genre, showtimes=showtimes)
            self.movies.update({movie_name: new_movie})

        self.scraped = True

    def get_movie_names(self):
        return self.movies.keys()

    def scrape_if_not_scraped(self):
        if not self.scraped:
            self.scrape()
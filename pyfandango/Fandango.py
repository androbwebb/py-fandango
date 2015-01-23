import requests
import feedparser
from services.Theater import Theater


class Fandango():
    def __init__(self):
        self.theaters = []

    def theaters_near(self, zip):
        if not zip or len(zip) < 5:
            raise Exception("Zipcode must be given")

        tree = feedparser.parse("http://www.fandango.com/rss/moviesnearme_{zip}.rss".format(zip=zip))

        for theater in tree['entries']:
            self.theaters.append(Theater(theater['title'], theater['link'], theater['description'], False))

        return self.theaters

if __name__ == "__main__":
    f = Fandango()
    print f.theaters_near("02135")

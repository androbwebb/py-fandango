# py-fandango
A fandango feed parser for Python

What makes this library different is the ability to [switch to scraping](https://github.com/androbwebb/pyfandango/blob/master/README.md#oh-so-you-want-showtimes-too-huh) for a portion of the site that isn't accessible to the API

## Installation
`pip install git+git://github.com/androbwebb/pyfandango.git`

#### Example
```python
from pyfandango.Fandango import Fandango

f = Fandango()
f.theaters_near("02135")  # 02135 = Boston

# Fandango.theaters_near returns a list of Theater Objects, but also saves it in the instance.theaters list
# f.theaters now holds a list of Theater Objects.
for t in f.theaters:
  print t.title
  for m in t.movies:
    # Movies are stored in Theater.movies as key => value. <Movie Name> => <Movie Object>. For quick lookups
    print "\t" + m
```

#### Output
```
Regal Fenway Stadium 13 & RPX
	Daryl Hall & John Oates: Recorded Live From Dublin
	Fifty Shades of Grey
	...
	Mortdecai
AMC Loews Boston Common 19
	Fifty Shades of Grey
	The Imitation Game
	Inherent Vice
	...
	Night at the Museum: Secret of the Tomb
Coolidge Corner Theatre
	Trailer Apocalypse
	...
	Inherent Vice
````


#### Oh, so you want showtimes too, huh?
Fandango API seems to be down/inactive or maybe they're just denying all applications. So instead of using the API, pyfandango scrapes the correct page. This should obviously be done sparingly, so don't overscrape.

#### Examples
- Want to find out when a movie is playing at a given theater:
```python
from pyfandango.Fandango import Fandango

def find_movie(movie_name, theater_id, zip_code):
  f = Fandango()
  f.theaters_near(zip_code)

  # Find correct theater
  for t in f.theaters:
    if t.id = theater_id:
      theater = t
  
  # Scrape this theater now (all movies/showtimes are scraped at once)
  theater.scrape_if_not_scraped()
  
  print ", ".join(theater.movies[movie_name].showtimes)
```

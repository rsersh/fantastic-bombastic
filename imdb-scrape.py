"""Bite 30. Movie data analysis
In this Bite we are going to parse a csv movie dataset to identify the directors with the highest rated movies.

Write get_movies_by_director: use csv.DictReader to convert movie_metadata.csv into a (default)dict of lists of Movie namedtuples. Convert/filter the data:
            Only extract director_name, movie_title, title_year and imdb_score.
            Type conversions: title_year -> int / imdb_score -> float
            Discard any movies older than 1960.

        Here is an extract:

        ....
        { 'Woody Allen': [
            Movie(title='Midnight in Paris', year=2011, score=7.7),
            Movie(title='The Curse of the Jade Scorpion', year=2001, score=6.8),
            Movie(title='To Rome with Love', year=2012, score=6.3),  ....
            ], ...
        }

+ Write the calc_mean_score helper that takes a list of Movie namedtuples and calculates the mean IMDb score, returning the score rounded to 1 decimal place.
+ Complete get_average_scores which takes the directors data structure returned by get_movies_by_director (see 1.) and returns a list of tuples (director, average_score) ordered by highest score in descending order. Only take directors into account with >= MIN_MOVIES

See the tests for more info. This could be tough one, but we really hope you learn a thing or two. Good luck and keep calm and code in Python!
"""
import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    dlist = []
    ddict = defaultdict(list)
    with open(MOVIE_DATA, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            director_name = row['director_name']
            if row['title_year'] != '':
                title_year = int(row['title_year'])
                if title_year > MIN_YEAR:
                    mt = Movie(row['movie_title'], title_year, float(row['imdb_score']))
                    dlist.append((director_name, mt))
    for k, v in dlist:
        ddict[k].append(v)
    return ddict


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    mean_score = mean([movie.score for movie in movies])
    return round(mean_score,1)



def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    avg_score_list = []
    for director in directors.keys():
        movie_list = directors[director]
        if len(movie_list) >= MIN_MOVIES:
            mean_score = calc_mean_score(movie_list)
            avg_score_list.append((director, mean_score))
    return sorted(avg_score_list,key=lambda score: score[1], reverse=True)

results = get_average_scores(get_movies_by_director())
print(results)

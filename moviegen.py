"""Bite 27. Parse omdb movie json data

    Working with APIs is very common these days and lucky for us they increasingly return JSON (over XML). We saved OMDb responses for some cool movies that the template code loads in.

    Parse this data answering some questions:

        get_movie_data should return a list of movie dicts, so for each movie you convert the json file to a dict.
        now you have the data structure, loop through the movies and return the movie:
            with Comedy in Genres (get_single_comedy)
            that had the most nominations (get_movie_most_nominations)
            having the longest runtime (get_movie_longest_runtime)

    Expect to do some string parsing and type conversions here. We hope you like it, enjoy!
    
APIs glob json movie data
from omdb import (get_movie_data, get_single_comedy,
                  get_movie_most_nominations, get_movie_longest_runtime)

movies = get_movie_data()


def test_movie_data_structure():
    assert len(movies) == 5
    assert all(type(m) == dict for m in movies)


def test_data_analysis():
    assert get_single_comedy(movies) == 'Horrible Bosses'
    assert get_movie_most_nominations(movies) == 'Fight Club'
    assert get_movie_longest_runtime(movies) == 'Blade Runner 2049'
"""

import glob
import json
import os
from urllib.request import urlretrieve
from operator import itemgetter

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movielist = []
    for moviefile in files:
        with open(moviefile) as fd:
            content = fd.read()
        moviedict = json.loads(content)
        movielist.append(moviedict)
    return movielist

def get_single_comedy(movies):
    movie = [ moviedict['Title'] for moviedict in movies if 'Comedy' in moviedict['Genre']]
    return movie[0]


def get_movie_most_nominations(movies):
    result = []
    movieslist = [ (m['Title'], m['Awards']) for m in movies ]
    for movie in movieslist:
        number = 0
        if ' nominations' in movie[1]:
            numberstr = movie[1].rstrip(' nominations.').lstrip()[-2:]
            number += int(numberstr)
        if 'Nominated ' in movie[1]:
            numberstr = movie[1].lstrip('Nominated for ')[0:2].rstrip()
            number += int(numberstr)
        else:
            number += 0
        result.append( (movie[0], number) )
    return [ (t,n) for t,n in sorted(result, key=itemgetter(1)) ][-1][0] 


def get_movie_longest_runtime(movies):
    movieslist = [ (m['Title'], m['Runtime']) for m in movies ]
    movies_stripped = [ (m[0], m[1].rstrip(' min')) for m in movieslist ]
    movies_w_runtimes = [ (m[0], int(m[1])) for m in movies_stripped]
    return [ (t,r) for t,r in sorted(movies_w_runtimes, key=itemgetter(1)) ][-1][0]


alist = get_movie_data()
print(get_single_comedy(alist))
print(get_movie_most_nominations(alist))
print(get_movie_longest_runtime(alist))


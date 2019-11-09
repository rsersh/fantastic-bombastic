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
    return [moviedict['Title'] for moviedict in iter(get_movie_data(movies)) if 'Comedy' in moviedict['Genre']][0]


def get_movie_most_nominations(movies):
    number_of_nominations = []
    result = []
    moviesgen = [ (m['Title'], m['Awards']) for m in iter(get_movie_data(movies)) ]
    for movie in moviesgen:
        if ' nominations' in movie[1]:
            number = int(movie[1].rstrip(' nominations.').lstrip()[-2:])
            number_of_nominations.append(number)
        if 'Nominated ' in movie[1]:
            number = int(movie[1].lstrip('Nominated for ')[0:2].rstrip())
            number_of_nominations.append(number)
        else:
            number_of_nominations.append(0)
        result.append( (movie[0], sum(number_of_nominations)) )
    return [ (t,n) for t,n in sorted(result, key=itemgetter(1)) ][-1][0] 


def get_movie_longest_runtime(movies):
    moviegen = iter(get_movie_data(movies))
    movies = [ (m['Title'], m['Runtime']) for m in moviegen ]
    return [ (t,r) for t,r in sorted(movies, key=itemgetter(1)) ][-1][0]

#alist = get_movie_data()
#print(alist[0])
print(get_single_comedy(files))
print(get_movie_most_nominations(files))
print(get_movie_longest_runtime(files))


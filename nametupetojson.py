"""Bite 13. Convert dict to namedtuple/json
    Write a function to convert the given blog dict to a namedtuple.
    Write a second function to convert the resulting namedtuple to json.
    Here you probably need to use 2 of the _ methods of namedtuple :)
    #dict #json #namedtuple
"""
from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
Sitetuple = namedtuple('Sitetuple', sorted(blog.keys()))

def encode_date(dto):
    if isinstance(dto, datetime):
        return str(dto.year) + ' ' + str(dto.month) + ' ' + str(dto.day)
    else:
        raise TypeError


def dict2nt(dict_):
    return Sitetuple(**dict_)


def nt2json(nt):
    sd = nt._asdict()
    return json.dumps(sd, default=encode_date)


st = dict2nt(blog)
js = nt2json(st)
print(f"Json output: {js}")


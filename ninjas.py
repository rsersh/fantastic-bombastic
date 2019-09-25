#! /usr/bin/python3

from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow':BeltStats(50,11),
             'orange':BeltStats(100,7),
             'green':BeltStats(175,1),
             'blue':BeltStats(250,5)}

def get_total_points(belts=ninja_belts):
    totalscore = 0
    for color in belts.keys():
        belt = belts[color]
        totalscore = totalscore + (belt.score*belt.ninjas)
    return totalscore


print(ninja_belts)
allpoints = get_total_points(ninja_belts)
print(allpoints)
#updates = dict('brown'=BeltStats(400,2),
#               'black'=BeltStats(600,5))
updates = {'brown':BeltStats(400,2), 'black':BeltStats(600,5)}
latest_ninjas = {**ninja_belts, **updates}
print(latest_ninjas)
newpoints = get_total_points(latest_ninjas)
print(newpoints)

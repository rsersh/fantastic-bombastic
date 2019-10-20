"""Bite 6. PyBites Die Hard
Given a listing of files of our community branch determine who PR'd (= submitted pull request) the most (excluding PyBites) and what challenge is the most popular (PR'd) as per snapshot of today (8th of Dec 2017).
See preparation done in the code template below. Replace pass with your code to make the test pass. Good luck and have fun!
Counter - file processing - generators - namedtuple

Checks community branch dir structure to see who submitted most
and what challenge is more popular by number of PRs"""

 
from collections import Counter, namedtuple
import os
import urllib.request


tempfile = os.path.join('/tmp', 'dirnames')
urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


def gen_files():
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)

    """
    line_gen = (row for row in open(tempfile))
    while True:
        try:
            #line_list = next(line_gen).split(',')
            line_list = next(line_gen)
            #if line_list[1] == "True\n":
            if line_list.endswith("True\n") == True:
                #yield (line_list[0].split('/'))[1]
                yield line_list
        except StopIteration:
            break


def diehard_pybites():
    user_gen = gen_files()
    while True:
        try:
            chal, user = next(user_gen).split(',')[0].split('/')
            if user not in IGNORE:
                users[user] += 1
                popular_challenges[chal] += 1
        except StopIteration:
            break
    mostprs = users.most_common(1)[0][0]
    mostchal = popular_challenges.most_common(1)
    d = Stats(user=mostprs, challenge=mostchal[0])
    return d



"""
dir_gen = gen_files()
while True:
    try:
        d = next(dir_gen)
        print(d)
    except StopIteration:
        break


try:
    u = diehard_pybites()
    print(u)
    #diehard()
except:
    print("There was a prob")

try:
    diehard()
    print(usercount.most_common(1))
except:
    print("There was a prob")
"""


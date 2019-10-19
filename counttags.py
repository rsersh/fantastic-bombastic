"""Get the top 10 blog tags of PyBites (e.g. python, flask, django, learning).

Our tests suppose you will use a collections.Counter - best practice and less code.
What are the PyBites guys most passionate about? See the tests and you'll know the answer, then code your solution to make them pass
Keep calm and code in Python! :)
#Counter #findall #regex

from tags import get_pybites_top_tags

def test_get_pybites_top_tags():
    expected = [('python', 79),
                ('learning', 79),
                ('codechallenges', 72),
                ('twitter', 62),
                ('tips', 61),
                ('flask', 52),
                ('news', 49),
                ('django', 37),
                ('code', 25),
                ('github', 24)]
    assert get_pybites_top_tags() == expected
    
"""
import os
from collections import Counter
import urllib.request
import re

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    cnt = Counter()
    pattern = re.compile(r'<category>(?:([\w\s]+))</category>')
    taglist = pattern.findall(content)
    for tag in taglist:
        cnt[tag] += 1
    return cnt.most_common(n)

tlist = get_pybites_top_tags()
print(tlist)
tlist = get_pybites_top_tags(3)
print(tlist)

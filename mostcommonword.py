"""Bite 18. Find the most common word
   Write a function that returns the most common (non stop)word in this Harry Potter text.

http://projects.bobbelderbos.com/pcc/harry.txt

  Make sure you strip out non-alphanumeric characters and stopwords. Your function should return a tuple of (most_common_word, frequency) (former lowercased).

  The template code already loads the Harry Potter text and list of stopwords in.

  Check the tests for more info - have fun!
 # Counter # data analysis # list comprehensions
 
from harry import get_harry_most_common_word


def test_get_harry_most_common_word():
    top_word = get_harry_most_common_word()
    assert type(top_word) == tuple
    assert top_word[0] == 'dursley'
    assert top_word[1] == 45
 
 """

import os
import urllib.request
from collections import Counter
import re

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    with open(stopwords_file, 'r') as fd:
        stopwords = fd.read()
    stopwordlist = stopwords.lower().split('\n')
    
    with open(harry_text, 'r') as fd:
        text = fd.read()
    text = text.lower()

    pattern = re.compile(r"\w+'*\w+")
    textlist = pattern.findall(text)
    words = [x for x in textlist if x not in stopwordlist]
    
    wordcount = Counter(words)
    return wordcount.most_common(1)

result = get_harry_most_common_word()
print(result[0])


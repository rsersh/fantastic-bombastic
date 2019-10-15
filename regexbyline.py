#!/usr/bin/python

import re

TEXT = """
PyBites was founded 19th of December 2016. That means that today,
14th of October 2019 we are 1029 days old. Time flies when you code
in Python. Anyways, good luck with this Bite. What is your favorite editor?
"""

TEXT_WITH_DOTS = """
We are looking forward attending the next Pycon in the U.S.A.
in 2020. Hope you do so too. There is no better Python networking
event than Pycon. Meet awesome people and get inspired. Btw this
dot (.) should not end this sentence, the next one should. Have fun!
"""


def splitSentences(text):
    newtext = text.replace('\n', ' ').lstrip(' ').rstrip(' ')
    pattern = re.compile(r'(?<=[\.\?!])\s(?=[A-Z])')
    return pattern.split(newtext)

"""
result = splitSentences(TEXT)
for item in result:
    print(item)
"""

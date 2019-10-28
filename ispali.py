"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import codecs
import urllib.request

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    if len(word) <= 1:
        return False
    norm_word = word.strip().lower()
    pali = False
    word_as_list = [c for c in norm_word if c.isalnum()]
    reversed_letters = reversed(word_as_list)
    for i in range(len(word_as_list)):
        if word_as_list[i] == next(reversed_letters):
            pali = True
        else:
            pali = False
            break
    return pali


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words is None:
        words = load_dictionary()
    max_length = 0
    
    for phrase in words:
        if is_palindrome(phrase):
            if len(phrase) > max_length:
                max_length = len(phrase)
                max_word = phrase
    return max_word

 
#a = get_longest_palindrome()
isit = is_palindrome("A Toyota\u00B4s a toyota. ")
if isit is True:
    print("It is a palindrome")
else:
    print("Not a palindrome")
isit = is_palindrome("Toyota\u00b4s a toyota. ")
if isit is True:
    print("It is a palindrome")
else:
    print("Not a palindrome")

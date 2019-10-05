""" Write a function that rotates characters in a string, in both directions:
    if n is positive move characters from beginning to end, 
       e.g.: rotate('hello', 2) would return llohe
    if n is negative move characters to the start of the string, 
    e.g.: rotate('hello', -2) would return lohel
    See tests for more info. Have fun!
"""


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    return string[n:]+string[:n]
    pass

backtofront = rotate('bob and julian love pybites!', 15)
print(backtofront)
backtofront = rotate('pybites loves julian and bob!', -15)
print(backtofront)
backtofront = rotate('julian and bob!', len('julian and bob!'))
print(backtofront)
backtofront = rotate('julian and bob!', 100)
print(backtofront)
backtofront = rotate('bob!julian and', 100)
print(backtofront)


"""
Martin is preparing to pass an IQ test.
The most frequent task in this test is to find out which one of the given characters differs from the others. He observed that one char usually differs from the others in being alphanumeric or not.
Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among non-alphanumerics or vice versa) among the given characters.
Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).
Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
Examples:
   ['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
   ['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
See the TESTS tab for more details

Martin's solution:
import string

alphanumeric_chars = list(string.ascii_letters + string.digits)


def get_index_different_char(chars):
    matches, no_matches = [], []
    for i, char in enumerate(chars):
        if str(char).lower() in alphanumeric_chars:
            matches.append(i)
        else:
            no_matches.append(i)
    return matches[0] if len(matches) == 1 else no_matches[0]
"""

def get_index_different_char(chars):
    smallalph = list('abcdefghijklmnopqrstuvwxyz')
    bigalph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nums = list(range(0,10))
    alphas = smallalph + bigalph + nums
    nonalphas = list("~`!@#$%^&*()-=_+[]{}\|;:,<.>?/'\"")
    alphacount = [x for x in chars if x in alphas]
    nonalphacount = [y for y in chars if y in nonalphas]
    
    if len(alphacount) > len(nonalphacount):  # look for nonalpha
        if '' in chars:
            return chars.index('')
        else:
            for item in chars:
                if item in nonalphas:
                    return chars.index(item)
    else:  # look for alpha
        for item in chars:
            if item in alphas:
                return chars.index(item)
    pass

a = ['A', 'f', '.', 'Q', 2]
b = ['.', '{', '^', '%', 'a']
c = [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c']
d = ['=','=', '', '/', '/', 9, ':', ';', '?', 'i'] #2 alphas
e = list(range(1,9)) + ['}'] + list('abcde')
f = [2, '.', ',', '!']

t = get_index_different_char(d)
print(t)

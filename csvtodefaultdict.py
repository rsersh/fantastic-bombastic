"""In this Bite you are presented with a list of surnames, names, and countries. These 3 fields are in a multiline string, separated by a comma.

    Code group_names_by_country, looping through the list, returning a collections.defaultdict where the keys are countries and the values are lists of concatenated names and surnames. The order of the names does not matter.

    Here is an example of a possible input to your function:

    ... and the output your function should return:

    defaultdict(,
                {'BR': ['Alphonso Harrold'],
                 'CN': ['Margo Apdell', 'Ines Parrett', 'Davie Halbard'],
                 'ID': ['Husain Watsham', 'Sula Wasielewski'],
                 'PL': ['Kermit Braunle'],
                 'RU': ['Deerdre Tomblings'],
                 'SE': ['Luke Brenston'],
                 'TD': ['Rudolph Jeffry']})

    Good luck and keep calm and code in Python! Read up on collections, one of our favorite standard library modules!

collections
defaultdict
groupby
"""
from collections import defaultdict

data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""
    
def group_names_by_country(datastring):
    d = defaultdict(list)
    #datalist = data.splitlines()
    #del datalist[0]
    datalist = data.splitlines()[1:]
    for item in datalist:
        last, first, country = item.split(',')
        d[country].append(first+ ' '+last)
    return d
    
mydict = group_names_by_country(data)
for k in mydict:
    print(f"{k} : {mydict[k]}")


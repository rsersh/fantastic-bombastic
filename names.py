NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names = list(map(lambda x: x.title(), names))
    # probably something better to do this
    # better way: return [x.title() for x in set(names)]
    # alternate: return list(set(name.title() for name in names))
    nameset = set(names)
    return list(nameset)
    pass


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    # better way: return sorted(names, key=lambda name: name.split()[1], reverse=True)
    names = dedup_and_title_case_names(names)
    newlist = [] 
    alphalist = []
    for name in names:
        first, last = name.split(' ')
        newlist.append(last+' '+first)
    newlist.sort(reverse=True)
    for name in newlist:
        last, first = name.split(' ')
        alphalist.append(first+' '+last)
    return alphalist
    pass


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # better way: return min([fname.split()[0] for fname in names], key=len)
    # or: return min(list(map(lambda s: s.split()[0], names)))
    min = 1000
    for name in names:
        first,last = name.split(' ')
        if len(first) < min:
            shortname = first
            min = len(first)
    return shortname 
    pass



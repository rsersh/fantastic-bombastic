"""Bite 80. Check equality of two lists

    In this Bite we compare two list objects for equality, a fundamental thing to understand in Python.

    Complete the check_equality function returning the various Enum values (representing equality scores) according to the type of equality of the lists:

        return SAME_REFERENCE if both lists reference the same object,
        return SAME_ORDERED if they have the same content and order,
        return SAME_UNORDERED if they have the same content unordered,
        return SAME_UNORDERED_DEDUPED if they have the same unordered content and reduced to unique items,
        and finally return NO_EQUALITY if none of the previous cases match.

    Have fun and keep calm and code in Python!
enum - equality - list
"""
from enum import Enum


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    if id(list1) == id(list2):
        return Equality(4)
    elif list1 == list2:
        return Equality(3)
    elif len(list1) == len(list2):
        z = [x for x in list1 if x not in list2]
        if len(z) == 0:
            return Equality(2)
        else:
            return Equality(0)
    elif len(list1) != len(list2):
        s1 = set(list1)
        s2 = set(list2)
        if s1 >= s2:
            return Equality(1)
        else:
            return Equality(0)
    else:
        return Equality(0)



#alist = [1,2,3] 
#blist = [4,5,6] 
#print(check_equality(alist, blist))
#alist = [1,2,3,4] 
#blist = alist 
#clist = alist[:] 
#print(check_equality(alist, blist))
#print(check_equality(alist, clist))
#elist = [1,2,3,4] 
#flist = [4,2,3,1] 
#print(check_equality(alist, elist))
a = [1,2,2,3,4] 
b = [1,2,2,3,4, 1,3,4,4] 
c = [1,2,2,3,4,1, 3, 4, 4, 5] 
print(check_equality(a, b))
print(check_equality(a, c))

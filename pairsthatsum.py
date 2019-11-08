"""Bite 208. Find the number pairs summing up N
In this Bite you complete find_number_pairs which receives a list of numbers and 
returns all the pairs that sum up N (default=10). Return this list of tuples from 
the function.
So in the most basic example if we pass in [2, 3, 5, 4, 6] it returns [(4, 6)] 
and if we give it [9, 1, 3, 8, 7] it returns [(9, 1), (3, 7)]. The tests check 
more scenarios (floats, other values of N, negative numbers).

Have fun and keep calm and code in Python
itertools, looping, numbers
TESTS TESTS
import pytest

"""
import itertools

def find_number_pairs(numbers, N=10):
    """
    resultlist = []
    pair_total = len(numbers) * len(numbers)-1
    perms = itertools.combinations(iter(numbers), r=2)
    for i in range(pair_total):
        tupe = next(perms)
        if sum(tupe) == N:
            resultlist.append(tupe)
    return resultlist
    """
    return [tupe for tupe in itertools.combinations(iter(numbers), r=2) if sum(tupe) == N]

nums = [4,2,3,5,0,1,10,11,7]
results = find_number_pairs(nums,5)
print(results)    

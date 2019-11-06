"""Bite 66. Calculate the running average of a sequence

Write a function that takes a sequence of items and returns the running 
average, so for example this:

running_mean([1, 2, 3])

returns:

	[1, 1.5, 2]

You can assume all items are numeric so no type casting is needed.
Round the mean values to 2 decimals (4.33333 -> 4.33). See the tests for more info.
Bonus: use a function of itertools + make it a generator, but this is not required 
to get this working.

import pytest

from running_mean import running_mean


@pytest.mark.parametrize("input_argument, expected_return", [
    ([1, 2, 3], [1, 1.5, 2]),
    ([2, 6, 10, 8, 11, 10],
     [2.0, 4.0, 6.0, 6.5, 7.4, 7.83]),
    ([3, 4, 6, 2, 1, 9, 0, 7, 5, 8],
     [3.0, 3.5, 4.33, 3.75, 3.2, 4.17, 3.57, 4.0, 4.11, 4.5]),
    ([], []),
])
def test_running_mean(input_argument, expected_return):
    ret = list(running_mean(input_argument))
    assert ret == expected_return
    
"""
import statistics as st
# from statistics import mean as mean

    
def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    # First soln without iter
    """
    run_list = []
    mean_list = []
    for i in sequence:
        run_list.append(i)
        result = st.mean(run_list)
        mean_list.append(round(result, 2))
    return mean_list
    """
    # Solution #2 with iter
    run_list = []
    mean_list = []
    s = iter(sequence)
    for i in range(len(sequence)):
        run_list.append(next(s))
        mean_list.append(round(st.mean(run_list),2))
    return mean_list 


alist = running_mean([1,2,3])
print('Return should be [1, 1.5, 2]')
print(alist) 
alist = running_mean([15, 16.5, 19, 211.25, 169.6, 157, 139.14285714285714, 132.753])
print('Return should be [15, 16.5, 19, 211.25, 169.6, 157, 139.14, 132.75]')
print(alist) 

"""Bite 188. Get statistics from PyBites test code
For this Bite we did a line count on our test code for 186 Bites, running this command: wc -l */test_*.py|sort -n -k2|grep -v total > testfiles_number_loc.txt. Output:

$ head -5 testfiles_number_loc.txt
    13 01/test_numbers.py
    17 02/test_regex.py
    23 03/test_wordvalue.py
    15 04/test_tags.py
    21 05/test_names.py
   ...

Complete the stats dict wih all the relevant metrics producing the following output:

    Basic statistics:
    - count     :     186
    - min       :       6
    - max       :     337
    - mean      :   43.74

    Population variance:
    - pstdev    :   43.04
    - pvariance : 1852.39

    Estimated variance for sample:
    - count     :   93.00
    """
from os import path
import statistics as st
# urlretrieve now listed in docs under Legacy Interface
# since it's ported from p2 may be deprecated in future
# 
from urllib.request import urlretrieve
import re

STATS = path.join('/tmp', 'testfiles_number_loc.txt')
if not path.isfile(STATS):
    urlretrieve('https://bit.ly/2Jp5CUt', STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""

pattern = re.compile(r'(^\d+)')

def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints
    # TODO 1: get the 186 ints from downloaded STATS file
    """
    line_count_list = []
    with open(data) as fd:
        content = fd.read()
    data_list = content.split('\n')
    for line in data_list:
        line_counts = pattern.findall(line.strip())
        if len(line_counts) > 0:
            line_count = int(line_counts[0])
            line_count_list.append(line_count)
    # even better:
    # with open(data) as f:
    #    return [int(lc.split()[0]) for lc in f.read().splitlines()]
    return line_count_list


def create_stats_report(data=None):
    if data is None:
        # converting to a list in case a generator was returned
        data = list(get_all_line_counts())
    # taking a sample for the last section
    sample = list(data)[::2]
    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = dict(count=len(data),
                 min_=min(data),
                 max_=max(data),
                 mean=st.mean(data),
                 pstdev=st.pstdev(data),
                 pvariance=st.pvariance(data),
                 sample_count=len(sample),
                 sample_stdev=st.stdev(sample),
                 sample_variance=st.variance(sample),
                 )

    return STATS_OUTPUT.format(**stats)    

#result = get_all_line_counts()
#print(result)
result = create_stats_report()
print(result)

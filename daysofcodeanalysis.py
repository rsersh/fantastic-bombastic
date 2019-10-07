# Written by Rachel R. Hunt Oct. 6, 2019 
# Provides analysis of daysofcodetracker.txt
# Each date is a one line entry in the file with 
# Date (MM-DD-YY), Minutes (xxx), Skills (python, git, flask) 
# provided in comma-separated string

import re

filename = "/home/chouchou/PyPlate/fantastic-bombastic/daysofcodetracker.txt"
pattern = re.compile(r',\s\d{2,3}')

totalminutes = 0

def grab_contentlist(fname):
    with open(fname, 'r') as fd:
        contentlist = fd.readlines()
    return contentlist

def print_content(alist):
    for item in alist:
        print(item)

def grab_number_of_days(alist):
    return (len(alist))-1 

# for now, out of commission
def check_last_item(alist):
    return [x for x in contentlist if x != ' \n']

def print_analysis(minutes, days):
    print('Analysis beginning for daysofcodetracker.txt...') 
    print(f'You have coded {minutes} minutes in {days} days!')
    hours =minutes/60
    print('Over %(hour)d hours so far!' % {'hour':hours})
    dailyavgmin = minutes/days
    print('That is an average of %(avgmin)d minutes per day ' % {'avgmin':dailyavgmin})
    dailyavghrs = minutes/days/60
    print('or over %(avghrs)d hours per day!' % {'avghrs':dailyavghrs})
    print('Keep coding, Rachel! You are mighty!')


contentlist = grab_contentlist(filename)
totaldays = grab_number_of_days(contentlist)
print_content(contentlist)
for item in contentlist:
    timeentrylist= pattern.findall(item)
    for entry in timeentrylist:
        daily = int(entry.lstrip(', '))
        totalminutes += daily

print_analysis(totalminutes, totaldays)

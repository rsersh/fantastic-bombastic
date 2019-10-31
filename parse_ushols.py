"""Bite 97. BeautifulSoup II - scrape US holidays

    In this Bite we use BeautifulSoup to scrape US holidays from OfficeHolidays to make a lookup of holidays per month.

    Check the HTML (here) for a table with CSS class list-table and parse its data. You need to populate the given holidays defaultdict like this:

      >>> from pprint import pprint as pp
      >>> from holidays import get_us_bank_holidays
      >>> pp(get_us_bank_holidays())
      defaultdict(,
                  {'01': ["New Year's Day", 'Martin Luther King Jr. Day'],
                   '02': ["Presidents' Day"],
                   '04': ['Emancipation Day'],
                   '05': ["Mother's Day", 'Memorial Day'],
                   '06': ["Father's Day"],
                   '07': ['Independence Day'],
                   '09': ['Labor Day'],
                   '10': ['Columbus Day'],
                   '11': ['Veterans Day', 'Thanksgiving', 'Day after Thanksgiving'],
                   '12': ['Christmas Day']})

    By the way, watch out for trailing spaces when parsing the holidays. Have fun and keep coding in Python!
    beautifulsoup defaultdict dict
"""
from collections import defaultdict
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    #soup = BeautifulSoup(f)
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.table.find_all('tr')
    holiday_list = []
    for i in range(1,len(rows)):
        month = rows[i].time.get_text()[5:7]
        hol = rows[i].a.get_text().strip()
        holiday_list.append((month,hol))
    for m,h in holiday_list:
        holidays.setdefault(m, []).append(h)
    return holidays
     

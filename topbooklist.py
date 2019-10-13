"""Get the most recommended books
The Tim Ferriss Show is full of wisdom and inspiration. It can also fill up your book shelves because a lot of awesome titles get recommended.
This raises the question: which books to prioritise? We found this list but for some the Top Books (2 or more mentions) might still be daunting!
Luckily we are PyBites Ninjas so what if we use some BeautifulSoup to scrape this site (we'll use a static copy) for the books that are at the top of this Top Books list.
Complete get_top_books below to find the number (limit) of books we could prioritise. Not surprisingly Sapiens is one of them :)
"""
from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
TIM_BLOG = 'https://bit.ly/2NBnZ6P'


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()
    soup = BeautifulSoup(content, 'html.parser')
    atags = soup.find_all('a')
    titleCounter = Counter()
    # ugliness below - range could break
    for i in range(303):
        link_to_check = atags[i]['href']
        if link_to_check.count(AMAZON) > 0:
            titleCounter[atags[i].get_text()] += 1    
    return [x[0] for x in titleCounter.most_common(limit)]
    

alist = get_top_books()
for item in alist:
    print(item)

import requests

YOUR_KEY = 'YOUR_PERSONAL_API_KEY_GOES_HERE'
DEFAULT_LIST = 'hardcover-nonfiction'

URL_NON_FICTION = (f'https://api.nytimes.com/svc/books/v3/lists/current/'
                   f'{DEFAULT_LIST}.json?api-key={YOUR_KEY}')
URL_FICTION = URL_NON_FICTION.replace('nonfiction', 'fiction')
weeksonlist = []

def get_best_seller_titles(url=URL_FICTION):
    #Use the NY Times Books API endpoint above to get the titles that are
    # on the best seller list for the longest time.
    r = requests.get(url)
    jsondata = r.json()
    resultdict = jsondata['results']
    books = resultdict['books']
    for entry in books:
        title, weeks = entry['title'], entry['weeks_on_list']    
        weeksonlist.append((title,weeks))
    return weeksonlist 
    pass


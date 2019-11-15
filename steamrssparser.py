"""Bite 55. Get the latest game releases from Steam's RSS feed

The Steam gaming platform has an RSS feed of their latest game releases. 
In this Bite, you'll pull down and parse that feed.

Specifically, pull out the names of the games in the feed as well as their 
URLs. Use the Game namedtuple provided.

To make sure you work with a static feed we copied today's version so use the 
URL defined in FEED_URL. Enjoy!

"""

from collections import namedtuple
import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    steamfeed = feedparser.parse(FEED_URL)
    entries = steamfeed['entries']
    return [Game(entry['title'], entry['link']) for entry in entries] 

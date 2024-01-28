import feedparser

def fetch_rss_data(url):
    feed = feedparser.parse(url)
    print("Feed Title:", feed.feed.title)
    for entry in feed.entries:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Published Date:", entry.published)
        print("Entry Summary:", entry.summary)
        print("\n")

rss_feed_urls = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

for url in rss_feed_urls:
    fetch_rss_data(url)

from feedparser import feedparser

fp = feedparser()

f1 = feedparser.search('Terrorism OR protest OR political unrest OR riot')

for entry in f1["entries"]:
    print(entry["title"])
    print(entry["link"])
    print(entry["summary"])

f2 = feedparser.search('positive OR uplifting')
for entry in f2["entries"]:
    print(entry["title"])
    print(entry["link"])
    print(entry["summary"])

f3 = feedparser.search('Natural Disaster')
for entry in f3["entries"]:
    print(entry["title"])
    print(entry["link"])
    print(entry["summary"])

f4 = feedparser.search('others')
for entry in f4["entries"]:
    print(entry["title"])
    print(entry["link"])
    print(entry["summary"])


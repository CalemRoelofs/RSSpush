import feedparser
import re
import textwrap
import unidecode
import datetime
from links import links

today = datetime.datetime.now()
now = today.strftime('%A')

if now == "Monday":
	python_wiki_rss_url = links[0]
elif now == "Tuesday":
	python_wiki_rss_url = links[1]
elif now == "Wednesday":
	python_wiki_rss_url = links[2]
elif now == "Thursday":
	python_wiki_rss_url = links[3]
elif now == "Friday":
	python_wiki_rss_url = links[4]
elif now == "Saturday":
	python_wiki_rss_url = links[5]
else:
	python_wiki_rss_url = links[6]

feed = feedparser.parse(python_wiki_rss_url)

for f in feed["items"]:
	print(f["title"])
	print(f["link"])
	print("\n")
	s = f["summary"]
	s = re.sub('<.+?>','',s)
	s = re.sub('&.+?;','',s)
	s = unidecode.unidecode(u'{}'.format(s))
	s = s[:-14]
	print(s)
	print("\n")
	print("=============================================================")
	print("\n")





import feedparser
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
from bs4 import BeautifulSoup

print(llog['feed']['title'])

post = llog.entries[2]
print(post.title)


content = post.content[0].value
print(content[:70])

cleaned = BeautifulSoup(content, "html.parser").get_text()
print(cleaned)
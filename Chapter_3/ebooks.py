from __future__ import division
import nltk, re, pprint

# url = "https://www.gutenberg.org/cache/epub/2554/pg2554.txt"
# raw = urlopen(url).read()

with open("cap.txt","r", encoding="utf-8") as dosto:
    book = dosto.readlines()

print(book[1020:1060])


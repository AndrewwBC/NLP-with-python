from __future__ import division
import nltk, re, pprint
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()

text = BeautifulSoup(html, "html.parser").get_text()
tokens = nltk.word_tokenize(text)

gene = nltk.Text(tokens).concordance("gene")

print(gene)

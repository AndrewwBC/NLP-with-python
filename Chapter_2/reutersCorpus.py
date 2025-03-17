from nltk.corpus import reuters

reuters.fileids()

# print(reuters.categories('training/9880'))
# print(reuters.fileids('barley')[:3])
print(reuters.words('training/1067'))

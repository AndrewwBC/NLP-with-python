import nltk
from nltk.corpus import inaugural

ids = inaugural.fileids()

years = [fileid[:4] for fileid in ids]

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))
cfd.plot()



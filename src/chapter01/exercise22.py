from nltk.book import *
from nltk import FreqDist

samples = [w for w in text5 if len(w) == 4]
f = FreqDist(samples)

print(f)

top50 = f.most_common()[:50]

print(top50)

import matplotlib.pyplot as plt
from nltk.book import *

samples = [w for w in text5 if len(w) == 4]
f = FreqDist(samples)

print(f)

top50 = f.most_common()[:50]

print(top50)

f.plot(50, cumulative=True)
plt.show()

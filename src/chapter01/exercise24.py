from nltk.book import *

a = [w for w in text6 if w.endswith("ize")]

b = [w for w in text6 if "z" in w]

c = [w for w in text6 if "pt" in w]

d = [w for w in text6 if w.istitle()]

print(a)
print(b)
print(c)
print(d)

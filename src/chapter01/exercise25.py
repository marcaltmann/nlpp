sent = ["she", "sells", "sea", "shells", "by", "the", "sea", "shore"]

a = [w for w in sent if w.startswith("sh")]
print(a)

b = [w for w in sent if len(w) > 4]
print(b)

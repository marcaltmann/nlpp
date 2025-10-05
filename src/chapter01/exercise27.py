from nltk.book import *
from nltk import Text


def vocab_size(text: Text):
    return len(set(text))


print(vocab_size(text1))

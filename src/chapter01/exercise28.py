from nltk.book import *
from nltk import Text


def percent(word: str, text: Text):
    word_count = text.count(word)
    text_length = len(text)
    return 100 / text_length * word_count


print(percent("whale", text1))

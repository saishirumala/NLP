
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "runner", "runs", "easily", "fairly", "studies", "studying"]

for word in words:
    print(word, "->", ps.stem(word))

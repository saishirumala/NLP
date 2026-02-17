import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')

words = ["running", "flies", "easily", "studies"]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Word\tStem\tLemma")
for word in words:
    print(word, "\t", stemmer.stem(word), "\t", lemmatizer.lemmatize(word))


from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

word = "mice"
# nltk.download("wordnet")

# Stemming
porter = PorterStemmer()
print(porter.stem(word))

# Lemmatization
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(word))
print(lemmatizer.lemmatize(word, pos=wordnet.VERB))  # pos -> parts-of-speech

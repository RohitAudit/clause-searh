from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk

f = open("out_text.txt", "r")
text = f.read().split(".\n\n")
arr = []
for i in text:
	arr.append(i)
	
arr2 = []
for j in arr:
	if 'Director' in j or 'Directors' in j:
		arr2.append(j)

stop = stopwords.words("english")



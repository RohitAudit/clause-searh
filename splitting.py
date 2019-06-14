from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

f = open("out_text.txt", "r")
text = f.read().split(".\n\n")
arr = []
for i in text:
	arr.append(i)


arr2 = []
a = 1
for j in arr:
	if 'Director' in j or 'Directors' in j:
		arr2.append(j)
		
		#np.concatenate(arr3,word_tokenize(j))
vectorizer = TfidfVectorizer(use_idf=True, lowercase=True,stop_words='english')		
X = vectorizer.fit_transform(arr2)	
kmeans = KMeans(n_clusters=2,init='k-means++',max_iter=100).fit(X)

arr3 = kmeans.labels_
print(arr2[0])





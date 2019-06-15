from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

def powerDir(txtfile):
	f = open(txtfile, "r")
	text = f.read().split(".\n\n")
	arr = []
	for i in text:
		arr.append(i)

	arr2 = []
	a = 1
	for j in arr:
		if 'Director' in j:
			arr2.append(j)

	vectorizer = TfidfVectorizer(use_idf=True, lowercase=True,stop_words='english')		
	X = vectorizer.fit_transform(arr2)	
	kmeans = KMeans(n_clusters=2,init='k-means++',max_iter=100).fit(X)

	arr3 = kmeans.labels_
	outfile = "power.txt"
	outfile2 = "notpower.txt"
	file = open(outfile,"a")
	file2 = open(outfile2,"a")
	for i,val in enumerate(arr3):
		if val == 1:
			file.write(arr2[i])
		else:
			file2.write(arr2[i])

	file.close()
	file2.close()
		

		






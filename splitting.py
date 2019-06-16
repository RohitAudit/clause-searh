from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
'''
Seperating clauses that define Power of Director
'''

def powerDir(txtfile):
	#opening output file from pdf's
	f = open(txtfile, "r")
	#splitting text into clauses
	text = f.read().split(".\n\n")
	arr = []
	for i in text:
		arr.append(i)

	arr2 = []
	a = 1
	
	#Clauses containing the phrase Director
	for j in arr:
		if 'Director' in j:
			arr2.append(j)
	# removing stop words and creating bag of frequency matrix
	vectorizer = TfidfVectorizer(use_idf=True, lowercase=True,stop_words='english')		
	X = vectorizer.fit_transform(arr2)	
	# performing K-means clustering
	kmeans = KMeans(n_clusters=2,init='k-means++',max_iter=100).fit(X)
	# labels assigned after K-means clustering
	arr3 = kmeans.labels_
	
	#output file 
	outfile2 = "power.txt"
	outfile = "notpower.txt"
	file = open(outfile,"a")
	file2 = open(outfile2,"a")
	for i,val in enumerate(arr3):
		if val == 1:
			file.write(arr2[i])
		else:
			file2.write(arr2[i])

	file.close()
	file2.close()
		

		







f = open("out_text.txt", "r")
text = f.read().split(".\n\n")
arr = []
for i in text:
	arr.append(i)
	
print(arr[127])
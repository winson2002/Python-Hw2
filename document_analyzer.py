def document_analyzer():
	words = []
	with open('document.txt', 'r') as f:

		for i in f:
			words.extend(i.split())

	from collections import Counter

	counts = Counter(words)
	five = counts.most_common(5)
	for i in five:
		print(five, ': ', counts) 

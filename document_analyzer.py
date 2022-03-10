def document_analyzer():
	file = open('document.txt','r')
	word = ''
	count = 0
	list = []

	for i  in file:
		line = i.lower().replace(',','').replace(':','').replace(',','').replace(';','').replace('(','').replace(')','').split(' ')

		for j in line:
			list.append(j)

	for x in range(0, len(list)):
		counts = 1
		for y in range(x+1, len(list)):
			if(list[x] == list[y]):
				counts += 1
		if counts > count:
			count = counts
			word = list[x]

	print(f'{word}: {count}')

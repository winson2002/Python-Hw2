def document_analyzer():
	file = open('document.txt','r')
	dic = {}

	for i in file:
		paragraph = i.replace('\n','').replace(',','').replace(':','').replace(',','').replace(';','').replace('(','').replace(')','').split(' ')

		for j in paragraph:
			if j ==  '':
				continue
			if j in  dic:
				dic[j] += 1
			else:
				dic[j] = 1
	print('')
	for y in range(5):
		word = ''
		if len(dic) == 0:
			return
		for x in dic:
			if word == '' or dic[x] > dic[word]:
				word = x
			elif dic[x] == dic[word] and word > x:
				word = x
		print(f'{word}: {dic[word]}')
		dic.pop(word)

	file.close()
document_analyzer()

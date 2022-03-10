def sort_list(list):
	n = len(list)
	i = 0
	while i < n:
		j = i+1
		while j < n:
			if list[i] > list[j]:
				list[i],list[j] = list[j],list[i]
			j+=1
		i+=1
	return(list)


a = [10,9,8,7,6,5,4,3,2,1,11,32,30]
print(sort_list(a))

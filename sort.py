def sort_list(list):
	n = len(list)
	i = 0
	while (i < n):
		j = n-i-1
		while (j < n):
			if (list[i] < list[j]):
				list[i], list[j] = list[j], list[i]
			j+=1
		i+=1
	return(list)

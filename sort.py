def sort_list(list):
	n = len(list)
	i = 0
	while (i < n):
		j = n-i-1
		while (j < n):
			if (list[i] > list[j]):
				{a[i],a[j] = a[j],a[i])
			j+=1
		i+=1
	return(list)

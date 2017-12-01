try:
	raw = input("Enter raw length : ")
	column = input("Enter column length : ")
	bin_list = []
	for i in range(0, raw):
		bin_list.append([])
		for j in range(0, column):
			bin_list[i].append(input("Enter list[" + str(i) + "][" + str(j) + "] th element : "))
	print bin_list
	list1 = [int(''.join(map(str, lis_data)), 2) for lis_data in bin_list]
	list2 = sorted(list(set(list1)))
	list_index = [list1.index(list2[-1]),list1.index(list2[-2])]
	list_out = [bin_list[x] for x in list_index]
	print 'List index : '+','.join(map(str,list_index))
	print 'Largest list : ', list_out
except Exception as ex:
	print ex

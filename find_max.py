import copy , datetime

print('-----分治法-----')
print('-----查找最大值-----')

two_element_list = []
test_list = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]

def divide_list(init_list):

	n = len(init_list)
	if n <= 2:
		two_element_list.append(init_list)
		return

	list_left , list_right = init_list[:n//2] , init_list[n//2:]
	divide_list(list_left)
	divide_list(list_right)
	return 

def get_max(init_list):
	return max(init_list[0],init_list[1])

def get_max_list(init_list):
	for i in range(len(init_list)):
		if len(init_list[i]) == 2:
			init_list[i] = get_max(init_list[i])
		else:
			init_list[i] = int(init_list[i][0])
	return init_list

def find_max(init_list):
	divide_list(init_list)
	s = copy.deepcopy(get_max_list(two_element_list)) 
	for i in range(len(two_element_list)):
		two_element_list.pop()
	n = len(s)
	if n == 1:
		return s
	return find_max(s)
	
starttime = datetime.datetime.now()
m = find_max(test_list)
endtime = datetime.datetime.now()
print(endtime-starttime)
print('最大值为：' + str(m[0]))



















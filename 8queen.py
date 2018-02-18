import time

def is_same_in_list(list_num):
	for i in list_num:
		if list_num.count(i)>=2:
			return True
		else:
			continue
	return False

def is_value_list(list_name):
	for a in range(1,len(list_name)):
		for i in range(len(list_name)-a):
			if (list_name[i]-list_name[i+a])**2 ==a**2:
				return True
			else:
				continue
	return False

def queen(z):
	solution = 0
	for a in range(1,z):
		for b in range(1,z):
			for c in range(1,z):
				for d in range(1,z):
					for e in range(1,z):
						for f in range(1,z):
							for g in range(1,z):
								for h in range(1,z):
									list1 = [a,b,c,d,e,f,g,h]
									if is_value_list(list1):
										continue
									else:
										if is_same_in_list(list1):
											continue
										else:
											solution += 1
	return solution

print('------八皇后问题-------')
print('------枚举法--------')

starttime = time.clock()
print(queen(9))
endtime = time.clock()
print(endtime-starttime)






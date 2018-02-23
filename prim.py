print('-----贪心算法-----')
print('-----prim计算最小生成树-----')

import random

used = []
INFINITY = 65536

def create_summits(num):
	new_list = []
	for i in range(1,num+1):
		new_list.append(i)
	return new_list

def add_summit(num):
	if num in used:
		return
	else:
		used.append(num)

def show(temp_last_element,temp_arr,temp):
	print(str(temp_last_element)+'->'+str(temp_arr)+':'+str(temp))


def find_lowest_summit(used):
	temp = INFINITY

	for row in used:
		for value in summits[row]:
			if temp > value and summits[row].index(value) not in used and value != 0:
				temp = value
				temp_arr = summits[row].index(value)
				temp_last_element = row

	show(temp_last_element,temp_arr,temp)
	
	add_summit(temp_arr)

	if set(used) == set(new):
		return

	return find_lowest_summit(used)

new = create_summits(6)
summits = [
	[INFINITY]
	,[INFINITY,0,6,1,5,]
	,[INFINITY,6,0,5,INFINITY,3]
	,[INFINITY,1,5,0,5,6,4]
	,[INFINITY,5,INFINITY,5,0,INFINITY,2]
	,[INFINITY,INFINITY,3,6,INFINITY,0,6]
	,[INFINITY,INFINITY,INFINITY,4,2,6,0]]

used.append(new[random.randint(0,5)])

find_lowest_summit(used)

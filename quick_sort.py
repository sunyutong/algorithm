import datetime

print('-----分治法-----')
print('-----快速排序-----')

def partition(seq):
	pi = seq[0]
	lo = [x for x in seq[1:] if x <= pi]
	hi = [x for x in seq[1:] if x > pi]
	return lo,pi,hi


def quick_sort(seq):
	if len(seq)<=1:
		return seq
	else:
		lo,pi,hi = partition(seq)
		return quick_sort(lo)+[pi]+quick_sort(hi)


seq = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]


starttime = datetime.datetime.now()
print(quick_sort(seq))
endtime = datetime.datetime.now()
print(str(endtime-starttime))
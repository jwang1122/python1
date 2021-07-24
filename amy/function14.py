def multiplyList(m) :
	res = 1
	for i in m:
		res = res * i
	return res

l = [8, 2, 3, -1, 7]

print(multiplyList(l))
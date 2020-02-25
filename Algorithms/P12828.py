def zerosAndOnes(n, l):
	if (n > 0):
		l.append(0)
		zerosAndOnes(n-1, l)
		l.pop()
		l.append(1)
		zerosAndOnes(n-1, l)
		l.pop()
	else:
		for e in l[:-1]:
			print(e, end=' ')
		print(l[-1])

n = int(input())
zerosAndOnes(n, [])

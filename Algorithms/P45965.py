#n total serie size
#o number of ones
#l backtracking list

def zerosAndOnes2(z, o, l):
	if (z != 0 or o != 0):
		if (z == 0):
			l.append(1)
			zerosAndOnes2(z, o-1, l)
			l.pop()
		elif (o == 0):
			l.append(0)
			zerosAndOnes2(z-1, o, l)
			l.pop()
		elif (z > 0 and o > 0):
			l.append(0)
			zerosAndOnes2(z-1, o, l)
			l.pop()
			l.append(1)
			zerosAndOnes2(z, o-1, l)
			l.pop()

	else:
		for e in l[:-1]:
			print(e, end=' ')
		print(l[-1])

import time

line = input()
start_time = time.time()
inputs = line.split()
o = int(inputs[1])
z = int(inputs[0]) - o 
zerosAndOnes2(z, o, [])
print("--- %s seconds ---" % (time.time() - start_time))

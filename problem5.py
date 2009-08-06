def divideByRange(n):
	counter = 0
	for i in range(1,20):
		if (n%i==0):
			counter += 1
	return counter==19

def problem5():
	smallest = 0
	i = 2520
	while (i < 1000000000):
		if (divideByRange(i) and smallest==0):
			smallest = i
		i += 2520
	return smallest

print "Problem 5 = %d" % problem5()
	
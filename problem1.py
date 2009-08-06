def problem1():
	x = 0
	for i in range (1, 1000):
		if (i%3 == 0 or i%5 == 0):
			x += i
	
	return x
	
	
print "Problem 1 = %d" % problem1()
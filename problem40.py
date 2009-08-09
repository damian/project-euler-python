def fraction():
	x = ''
	for i in range(1,1000000):
		x += str(i)
	return list(x)
	

def problem40():
	array = fraction()
	result = int(array[0])
	const, index = '9', 9
	while (index < 1000000):
		result *= int(array[index])
		index = int(str(index) + const)		
	return result

print "Problem 40 = %d" % problem40()


	
	
	

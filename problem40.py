def fraction():
	x = ''
	for i in range(1,1000000):
		x += str(i)
	return list(x)
	

def problem40():
	array = fraction()
	result = int(array[0])
	result *= int(array[9])
	result *= int(array[99])
	result *= int(array[999])
	result *= int(array[9999])
	result *= int(array[99999])
	result *= int(array[999999])
	return result

print "Problem 40 = %d" % problem40()


	
	
	

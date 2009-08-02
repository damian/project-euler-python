def fibonacci(n):
	result = 0
	x = 1
	old = 0
	old1 = 1
	while (x < n):
		x = old + old1
		old = old1
		old1 = x
		if (x%2==0):
			result += x 
	return result

def problem2():
	return fibonacci(4000000)
	
print problem2()

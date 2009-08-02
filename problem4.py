def palendrome(word):
	return str(word) == (str(word))[::-1]
	
def problem4(n):
	biggest = 10000
	for i in range(100,n):
		for j in range(100, n):
			x = i * j
			if (palendrome(x) and x > biggest):
				biggest = x
	return biggest

print "Answer = %d" % problem4(999)
	
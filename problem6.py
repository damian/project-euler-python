def square(x):
	return x**2
 
def sumOfSquares(n):
	return sum(map(square, makeArray(n)))

def squareOfSum(n):
	return square(sum(makeArray(n)))
	
def makeArray(n):
	array = []
	for i in range (1,n+1):
		array.append(i)
	return array
 
def problem6(n):
  return squareOfSum(n) - sumOfSquares(n)
 
print "Problem 6 = %d" % problem6(100)


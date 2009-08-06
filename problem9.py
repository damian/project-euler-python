def problem9():
	upper = 1000
	answer = 0
  
	for a in range(1,upper):
		for b in range(1,upper):
			if (a+b<upper and a<b):
				c=upper-(a+b)
				if (a+b+c==upper and pythaogoreanTriplet(a,b,c)):
					answer = a*b*c
	return answer

 
def pythaogoreanTriplet(a,b,c):
  return a**2+b**2==c**2
 
print "Problem 9 = %d" % problem9()
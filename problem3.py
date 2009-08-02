import math

def sieve(n):
	siv=range(n+1)
	siv[1]=0
	sqn=int(round(n**0.5))
	for i in range(2,sqn+1):
		if siv[i]!=0:
			siv[2*i:n/i*i+1:i]=[0]*(n/i-1)
			
	return filter(None,siv)
	
def problem3(n):
	return filter(lambda p: n%p==0, sieve(int(math.sqrt(n))))[-1]
	
print "Answer = %d" % (problem3(600851475143))

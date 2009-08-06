def sieve(n):
	siv=range(n+1)
	siv[1]=0
	sqn=int(round(n**0.5))
	for i in range(2,sqn+1):
		if siv[i]!=0:
			siv[2*i:n/i*i+1:i]=[0]*(n/i-1)
			
	return filter(None,siv)

def problem7():
	return sieve(250000)[10000]

print "Problem 7 = %d" % problem7()
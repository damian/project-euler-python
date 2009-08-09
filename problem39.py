def problem39():
	a,b,c = 1,1,1
	hash = {}
	for	a in range(1,997):
		b = a
		for b in range(b,997):
			c = b
			for c in range(c, 997):
				if (a + b + c <= 1000) and (a*a + b*b == c*c):
					result = a + b + c
					if (hash.has_key(result)):
						hash[result] += 1
					else:
						hash[result] = 1
	e = hash.keys()
	e.sort(cmp = lambda a,b: cmp(hash[a],hash[b]))
	return e[-1]	
	
print "Problem 39 = %d" % problem39()
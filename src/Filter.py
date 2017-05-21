def step(t, a):	
	return t >= a
	
def pulse(x, i, r): 
	return step(x, i) - step(x, i+r)

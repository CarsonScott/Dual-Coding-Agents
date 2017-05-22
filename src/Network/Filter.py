def step(value, interval):	
	return value >= interval
	
def pulse(value, origin, radius): 
	return step(value, origin-radius) - step(value, origin+radius)


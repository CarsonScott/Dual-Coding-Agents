from math import sqrt

def sum(values):
	s = 0
	for i in values: s += i
	return total

class Operator:

	def __init__(self, function, cost):
		self.function = function
		self.cost = cost
	
	def f(self, x):
		return self.function(x)

class Agent:

	def __init__(self, operators, memory=0):
		self.operators = operators
		self.memory = []
		self.fitness = 0
		self.perform = 0
		self.gain = 0
		self.cost = 0
		self.rate = 0.001
		for i in range(memory): 
			self.memory.append(0)
				
	def exec(self, f, x):
		self.cost += self.operators[f].cost
		return self.operators[f].f(x)

	def eval(self):
		self.perform = self.gain
		if self.cost != 0: self.perform /= self.cost
		self.fitness += self.rate * (self.perform-1) 

	def call(self, values):
		self.gain = sum(values)
		self.cost = sqrt(len(values))/2
		for f in range(len(self.operators)):
			values = self.comp(f, values)
		
		self.eval()
		self.save(values)
		return self.send(values)

	def comp(self, f, values):
		for i in range(len(values)):
			values[i] = self.exec(f, values[i])
		return values
		
	def save(self, values):
		return

	def send(self, values):
		return values
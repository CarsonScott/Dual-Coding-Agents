class Node:
	
	def __init__(self):
		self.value = 0
	
	def output(self, value):
		return value
	
	def memory(self, value):
		self.value = value
	
	def update(self, value):
		output = self.output(value)
		self.memory(value)
		return output

class DelayNode(Node):
	def output(self, value):
		return self.value

class DeltaNode(Node):
	def output(self, value):
		return value - self.value

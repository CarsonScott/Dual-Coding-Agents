from Node import *

class Set:

	def __init__(self, length):
		self.nodes = []
		self.values = []
		for i in range(length):
			self.values.append(0)
			self.nodes.append(self.create())
	def value(self, node, value):
		return value
	def update(self, value):
		for i in range(len(self.values)):
			self.memory(i,self.compute(i,self.value(i, value)))
		return self.output()
	def compute(self, node, value):
		return self.nodes[node].update(value)
	def memory(self, index, value):
		self.values[index] = value
	def output(self):
		return self.values
	def create(self):
		return Node()

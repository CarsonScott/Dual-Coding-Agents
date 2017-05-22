from Set import *

class Link(Set):
	def value(self, node, value):
		if node == 0: return value
		return self.values[node-1]
	def output(self):
		return self.values[len(self.values)-1]
	def update(self, value):
		for i in range(len(self.values)):
			self.memory(i, self.compute(i, self.value(i, value)))
		return self.output()
	
class DelayLink(Link):
	def create(self):
		return DeltaNode()

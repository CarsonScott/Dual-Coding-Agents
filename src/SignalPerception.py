from Filter import step, pulse

class DelayPort:

	def __init__(self):
		self.value = 0

	def update(self, value):
		output = self.value
		self.value = value
		return output

class DelayLine:

	def __init__(self, length):
		self.ports = []
		for i in range(length):
			self.ports.append(DelayPort())

	def update(self, value):
		for i in range(len(self.ports)):
			value = self.ports[i].update(value)
		return value

class Converter:

	def __init__(self, sensors, signal_range):
		self.sensors = []
		self.range = signal_range
		self.radius = self.range / sensors

		for i in range(sensors):
			self.sensors.append(0)
		
	def compute(self, signal):
		for sensor in range(len(self.sensors)):
			self.sensors[sensor] = pulse(signal, sensor * self.radius, self.radius)
		return self.sensors
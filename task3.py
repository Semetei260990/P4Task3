class Car:
	def __init__(self, make, model, year, odometer, fuel):
		self.odometer = 0
		self.fuel = 70

	def __add_distance(self, km):
		self.odometer += km

	def __subtract_fuel(self, oil):
		self.fuel -=  oil

	def drive(self, km):
		if km/10 <= 70:
			oil = km/10
			self.__add_distance(km)
			self.__subtract_fuel(oil)
			print('Lets drive')
		else:
			print('Need more fuel, please, fill more')

Honda = Car('BMW', 'X', 2005, 0, 70)
Honda.drive(100)
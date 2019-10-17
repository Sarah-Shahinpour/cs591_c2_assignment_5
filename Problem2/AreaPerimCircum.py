import math

class AreaPerimCircum():


	def __init__(self):
		pass


		# Reference: https://stackabuse.com/getting-user-input-in-python/
	def shape_select(self):
		shape = input("Choose a shape: (C)ircle or (R)ectangle or (S)quare  ")
		self.calculator(shape)


	def calculator(self, shape):
		if shape == "R":
			length = int(input("Rectangle length?  "))
			breadth = int(input("Rectangle breadth?  "))
			nums = self.rectangle(length, breadth)
			print("Area:", nums[0], "square units and Perimeter:", nums[1], "units")
		elif shape == "S":
			length = int(input("Square length?  "))
			nums = self.square(length)
			print("Area:", nums[0], "square units and Perimeter:", nums[1], "units")
		elif shape == "C":
			radius = int(input("circle radius?  "))
			nums = self.circle(radius)
			print("Area:", nums[0], "square units and Circumference:", nums[1], "units")
		else:
			error = self.invalid()
			print(error)


	def rectangle(self, l, w):
		area = l*w
		perimeter = 2*l + 2*w
		return [area, perimeter]


	def square(self, s):
		area = s**2
		perimeter = 4*s
		return [area, perimeter]


	def circle(self, r):
		area = math.pi*r**2
		circumference = 2*math.pi*r 
		return [area, circumference]


	def invalid(self):
		return "Invalid shape selection!"

# a = AreaPerimCircum()
# a.shape_select()


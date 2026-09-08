'''
# Sample class with init method
class Person:
	# init method or constructor
	def __init__(self):
		self.name = "Arockia"

	#def __del__(self):
	#	print("Object is deleted")

    # Sample Method
	def printname(self):
		print('Hello, my name is', self.name)
		
#Person().printname()

p = Person()
p.printname()

p.name = "Raja"
p.printname()

#del p

print("*****************************************")

'''
class Addition:
	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second

# creating object of the class
obj1 = Addition(10, 20)

# creating second object of same class
obj2 = Addition(40, 10)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()

print("*********************************************")

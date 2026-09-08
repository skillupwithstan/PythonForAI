# Exceptions
#5 * (1/0)
#(total * 3)

def divide(x, y):
	result = x // y
	print("The division value is :", result)

divide(5, 2)
divide(5, 0)

def divide(x, y):
	try:
		result = x // y
		print("The division value is :", result)
	except ZeroDivisionError:
		print("Sorry! You are dividing by zero")
	finally:
		print("Always run")

divide(5, 2)
divide(5, 0)

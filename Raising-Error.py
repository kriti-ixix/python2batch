try:
	length = int(input("Length: "))
	breadth = int(input("Breadth: "))

	if (length < 0 or breadth < 0):
		raise ValueError

except ValueError:
	print("Length and breadth cannot be in negative")

except:
	print("Error")
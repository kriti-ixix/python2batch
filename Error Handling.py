#Normal working of the program
try:
	#IndexError
	myList = [1, 2, 3, 4, 5, 6]
	print(myList[10])

	#KeyError
	myDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
	print(myDict[100])

#In case exception
except IndexError:
	print("Index error occured")

except KeyError:
	print("Key error occured")

except Exception as e:
	print("Error")

#Optional
finally:
	print("Execution finished")


'''
Types of Errors:

	• IndexError
	• ModuleNotFoundError
	• KeyError
	• ImportError
	• StopIteration
	• TypeError
	• ValueError
	• NameError
	• ZeroDivisionError
	• KeyboardInterrupt
	• FloatingPointError
	• MemoryError
	• OSError

'''
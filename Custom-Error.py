class Error(Exception):
	pass

class ValueTooSmallError(Error):
	pass

class ValueTooLargeError(Error):
	pass

number = 10

while True:
	try:
		guess = int(input("Enter your guess: "))

		if (guess<number):
			raise ValueTooSmallError 
		elif (guess>number):
			raise ValueTooLargeError
		else:
			print("You guessed correctly!")
			break

	except ValueTooLargeError:
		print("Guess was too high")

	except ValueTooSmallError:
		print("Guess was too low")

	except TypeError:
		print("Type Error Raised")

	except:
		print("Error")
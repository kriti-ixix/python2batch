import re

class Error(Exception):
	pass

class EmailError(Error):
	pass

class DomainError(Error):
	pass

class PasswordTooShortError(Error):
	pass

try:
	email = input("Enter your email: ") #abc@gmail.com
	listOfDomains = ['com', 'org', 'co.in', 'net']
	password = input("Enter your password: ")

	if '@' not in email:
		raise EmailError
	else:
		userDomain = email.split('.', 1)[-1]
		if userDomain not in listOfDomains:
			raise DomainError

	if len(password) < 6:
		raise PasswordTooShortError

except EmailError:
	print("@ is missing")

except DomainError:
	print("Domain is missing")

except PasswordTooShortError:
	print("Password is too short")

except Exception as e:
	print(e)

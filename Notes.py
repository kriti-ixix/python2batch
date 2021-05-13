filename = "My Notes.txt"

myFile = open(filename, 'r')

userChoice = "Note " + input("Which note do you want to read? ")

for line in myFile:
	if userChoice in line:
		print(line, end="")
		break
else:
	print("No note found")

'''
for num in range(1, 6):
	print(num)
else:
	print("End of statement")


['Line1', 'Line2', 'Line3', 'Line4']


[(2,'Line3'), (3,'Line4'), (0, 'Line1'), (1, 'Line2')]
'''
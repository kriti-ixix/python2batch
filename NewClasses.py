class StudentInfo():
	def __init__(self, newName="N/A", newRollno=0, newGender=""):
		self.rollno = newRollno
		self.name = newName
		self.marks = 0
		self.gender = newGender
		self.percentage = 0
		self.subjects = []

	def calculatePercentage(self):
		self.percentage = (self.marks/50) * 100

	def __str__(self):
		return str(self.rollno) + ". " + self.name


student1 = StudentInfo("Kriti", 123, "F")
student2 = StudentInfo("Sharan", 456, "F")
student3 = StudentInfo("XYZ", 345, "M")
student4 = StudentInfo()
#student3 = StudentInfo(input("Name: "), input("Roll no: "), input("Gender: "))

print(student1)
print(student2)
print(student3)
print(student4)

#print(student1.rollno, ".", student1.name, student1.gender)
#print(student2.rollno, ".", student2.name, student2.gender)

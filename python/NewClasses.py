#Parent/Base class
class StudentInfo():
	def __init__(self, newName, newRollno, newGender):
		self.rollno = newRollno
		self.name = newName
		self.gender = newGender
		self.subjects = []

	def calculatePercentage(self):
		self.percentage = (self.marks/50) * 100

	def __str__(self):
		return str(self.rollno) + ". " + self.name


#Child/sub class
class Marks(StudentInfo):
	def __init__(self, newMarks, newPercent, newSub, newName, newRollno, newGender):
		StudentInfo.__init__(self, newName, newRollno, newGender)
		self.marks = newMarks
		self.percentage = newPercent
		self.subjectName = newSub

	def __str__(self):
		return self.name + " got " + str(self.marks) + " in " + self.subjectName


subject1 = Marks(90, 90, "English", "ABC", 5, "F")
print(subject1)




'''
student1 = StudentInfo("Kriti", 123, "F")
student2 = StudentInfo("Sharan", 456, "F")
student3 = StudentInfo("XYZ", 345, "M")
student4 = StudentInfo()
#student3 = StudentInfo(input("Name: "), input("Roll no: "), input("Gender: "))

print(student1)
print(student2)
print(student3)
print(student4)
'''

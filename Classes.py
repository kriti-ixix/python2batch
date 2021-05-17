class StudentInfo():
	def __init__(self):
		self.rollno = 0
		self.name = ""
		self.marks = 0
		self.gender = ""
		self.percentage = 0
		self.subjects = []

	def calculatePercentage(self):
		self.percentage = (self.marks/50) * 100


student1 = StudentInfo()
student1.name = "Kriti"
student1.marks = 45
student1.calculatePercentage()
#print(student1.percentage)

student2 = StudentInfo()
student2.name = "Sharanpreet"
student2.marks = 50
student2.calculatePercentage()
#print(student2.percentage)

student3 = StudentInfo()
student3.name = "Harpreet"
student3.marks = 50
student3.calculatePercentage()
#print(student3.percentage)

listOfStudents = [student1, student2, student3]

for student in listOfStudents:
	print("{} got {}%".format(student.name, student.percentage))
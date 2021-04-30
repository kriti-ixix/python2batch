myList = ["A", "B", "C", "D"]

#Key : Value
myDict = {}
myDict = {"A":1, 2:"B", 3:"C", "D":4, 5:[1, 2, 3, 4]}

myDict["X"] = 5

print(myDict)
myDict['X'] = 100
print(myDict)

names = ["A", "B", "C", "D"]
rollno = [1, 2, 3, 4]
myDict = {}

for index in range(len(names)):
    myDict[rollno[index]] = names[index]

print(myDict)

myDict = {}

for i in range(5):
    rollno = int(input("Roll no: "))
    name = input("Name: ")
    myDict[rollno] = name

print(myDict)

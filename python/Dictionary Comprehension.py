'''
myDict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6}

#Returns only keys
for i in myDict:
    print(i)

#Returns both keys and values in tuples
for i in myDict.items():
    print(i)

list = []
dict/set = {}
tuple = () 
("A", 1) ("B", 2)

#Dictionary unpacking
for (i, j) in myDict.items():
    print("Key:", i)
    print("Value:", j)


myDict = {}

for num in range(1, 11):
    myDict[num] = num * num 

myDict = {num : num * num for num in range(1, 11)}

print(myDict)
'''

keysList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
valuesList = [10, 20, 30, 40, 50, 60, 70]

myDict = {}

for i in zip(keysList, valuesList):
    print(i)

for (i, j) in zip(keysList, valuesList):
    myDict[i] = j

print(myDict)

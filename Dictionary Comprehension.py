myDict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6}

#Returns only keys
for i in myDict:
    print(i)

#Returns both keys and values in tuples
for i in myDict.items():
    print(i)

'''
list = []
dict/set = {}
tuple = () 
("A", 1) ("B", 2)
'''

#Dictionary unpacking
for (i, j) in myDict.items():
    print("Key:", i)
    print("Value:", j)
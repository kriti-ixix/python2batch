stdNames = ["ABC", "XYZ", "PQR", "GHJ"]
emptyList = []
print(stdNames[2])

#Searching an element in a list
if "X" in stdNames:
    print("Found it!")
else:
    print("Didn't find anything")
    
#Adding an element
stdNames.append(123)
print(stdNames)

#Changing a value
stdNames[1] = 456
print(stdNames)

#Inserting a value
stdNames.insert(2, "JKL")
print(stdNames)

#Removing a value
stdNames.remove("JKL")
print(stdNames)

newList = list(range(100, 0, -1))
print(newList)
myList = []

for i in range(1, 11):
    if (i%2 == 0):
        myList.append(i)

print(myList)

myList = [i for i in range(1, 11) if (i%2==0)]
print(myList)
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def squared(num):
    return num*num

def checkEven(num):
    if num%2==0:
        return True
    else:
        return False

'''
for num in myList:
    squares.append(squared(num))

print(set(map(squared, myList)))
'''

l = lambda num : num * num

#print(list(map(lambda num : num * num, myList)))

print(list(filter(lambda x : x%2 == 0, myList)))

lambda x, y : x + y

#enumerate

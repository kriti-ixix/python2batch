'''
Functions are of two types based on input:
    - Default
    - Parameterised 
    
Based on return type:
    - No return
    - Some value is returned
'''
'''
#Function definition
def addTwo(first, second):
    #first = int(input("Enter first number: "))
    #second = int(input("Enter second number: "))
    third = first + second
    print("The sum is: ", third)
    
print("Addition!")
#Function calling
addTwo(5, 10)
addTwo(30, 20)
x = 40
y = 50
addTwo(x, y)
'''

def addTwo(first, second):
    third = first + second
    return third

x = addTwo(5, 10)
y = addTwo(20, 30)
print("The sums are ", x, " ", y)
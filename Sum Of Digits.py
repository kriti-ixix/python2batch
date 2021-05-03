number = int(input("Enter a number here: "))
sumOfDigits = 0
temp = number

'''
567
5 + 6 + 7

567%10 -> 7
0 + 7
567/10 -> 56

56%10 -> 6
7 + 6
56/10 -> 5

5%10 -> 5
13 + 5
5/10 -> 0
'''

while temp != 0:
    print("Number:", temp)
    remainder = temp%10
    print("Remainder", remainder)
    sumOfDigits += remainder
    print("Sum:", sumOfDigits)
    temp = int(temp/10)

#The sum of 567 is 18
print("The sum of {} is: {}".format(number, sumOfDigits))
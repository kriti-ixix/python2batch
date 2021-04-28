sumOfNumbers = 0
i = 0

limit = int(input("Enter a number: "))

while i<=limit:
    sumOfNumbers += i
    i += 1
    print("Value of i: ", i)
    print("Sum: ", sumOfNumbers)
    
    
#for i in range(limit+1)
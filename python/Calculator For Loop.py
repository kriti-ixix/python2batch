x = 5
y = 10
resultList = []

for i in range(5):
    choice = input("Enter an operator: ")

    if (choice == "+"):
        result = x + y
        resultList.append(result)
    
    elif (choice == "-"):
        result = x - y
        resultList.append(result)
    
    elif (choice == "*"):
        result = x * y
        resultList.append(result)
    
    elif (choice == "/"):
        result = x / y
        resultList.append(result)
    
    else:
        result = "Invalid"
        resultList.append(result)
        
    print(result)
                
print(resultList)

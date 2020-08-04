print("Please select operation -")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
num = int(input("Select operations form 1,2,3,4 : "))
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num == 1 :
    num3 = num1+num2
    print(num1,"+",num2,"=" ,num3)
elif num == 2 :
    num3 = num1-num2
    print(num1,"-",num2,"=" ,num3)    
elif num == 3 :
    num3 = num1*num2
    print(num1,"*",num2,"=" ,num3)
elif num == 4 :
    num3 = num1/num2
    print(num1,"/",num2,"=" ,num3)
else :
    print("ERROR")


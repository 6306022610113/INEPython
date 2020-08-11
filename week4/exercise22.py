number = int(input("Enter number : "))
column = int(input("Enter column munber : "))

for i in range(column):
    for num in range(number):
        print(num," ",end="")
    print()
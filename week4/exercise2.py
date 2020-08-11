num = int(input('Enter number : '))
column = int(input('Enter number column: '))

for i in range(column):
    for number in range(num):
        print(number," ",end="")
    print()
    
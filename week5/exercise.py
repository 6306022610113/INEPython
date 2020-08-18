fname = str(input('ENTER YOUR FIRST NAME : '))
lname = str(input('ENTER YOUR LAST NAME : '))
num = str(input('ENTER YOUR STUDENT ID NUMBER : '))

print('YOUR SYSTEM LOGIN NAME IS : ')
print(fname[:3]+lname[:3]+num[-3:])

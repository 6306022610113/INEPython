fname = input('ENTER YOUR FIRST NAME : ')
lname = input('ENTER YOUR LAST NAME : ')
num = input('ENTER YOUR STUDENT ID NUMBER : ')

print('YOUR SYSTEM LOGIN NAME IS : ')
print(fname[:3]+lname[:3]+num[-3:])

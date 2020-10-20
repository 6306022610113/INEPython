import random

a = ['cymbals','violin','guitar','library','office','restroom','art room','mountain',
    'rainbow','river','punk','reggae','blues','auditorium','gymnasium',
    'playground','classical','ambulance','motorcycle','bookstore','restaurant','supermarket']
mywrite = random.choice(a)
print(mywrite)
def write():

    y = input()
    if mywrite == y :
        print("Good")
    else:
        print("bad")
write()

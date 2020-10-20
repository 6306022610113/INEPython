import random 

print("What is my mad]gic number (1 or 100) ?")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
print(mynumber)
while ntries < 7 and mynumber != yourguess :
    msg = str(ntries) + ">> "
    if(ntries == 6) :
        print("Your last")
    yourguess = int(input(msg))

    if mynumber < yourguess :
        print("--> too high")
    else :
        print("--> too low")
    ntries += 1

if mynumber == yourguess:
    print("Yes! it's" ,mynumber)
else :
    print("Sorry! my number is" , mynumber)
def main():

    infile = open('numbers.txt','r')

    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    infile.close()

    #add the three numbers.
    total = num1 + num2 + num3

    #display the number and their total.
    print('The number are : ',num1,num2,num3)
    print('Their total is : ',total)

main()
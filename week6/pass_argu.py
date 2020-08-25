#this program demonstra tes a funtion that accepts
#two arguments.
def main():
    print('The sum of 12 and 45 is')
    num1 = int(input('number 1 : '))
    num2 = int(input('number 2 : '))
    show_sum(num1,num2)

#The show_sum function accepts two arguments
#and displays their sum.
def show_sum(num1,num2):
    result = num1 + num2
    print(result)

# call the main function.
main()
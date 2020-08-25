value = int(input('number : '))
def main():
    show_double(value)

#The show_double function accepts an argument
#and displays double its value
def show_double(number):
    result = number * 2
    print(result)

#call the main function.
main()
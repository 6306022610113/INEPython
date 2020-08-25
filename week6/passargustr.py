#This program demontrates passing two string
#argumant to a function.
def reverse_name(first , last):
    print(last, first)

def main():
    first_name = input('Enter your first name:')
    last_name = input('Enter your last name:')
    print('Your name reversed is')
    reverse_name(first_name,last_name)

#Call the main function
main()
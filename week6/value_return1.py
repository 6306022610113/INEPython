def get_name():
    #Get the user's first and last names.
    first = input('Enter your first name : ')
    last = input('Enter your last name : ')
    #Return both names.
    return first,last

first_name,last_name = get_name()
print('First name : ',first_name, 'Last name : ',last_name)
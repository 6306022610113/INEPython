def main():
    first_name,last_name = get_name()
    print('First name : ',first_name, 'Last name : ',last_name)
    print(password2(first_name,last_name))

def get_name():
    #Get the user's first and last names.
    first = input('Enter your first name : ')
    last = input('Enter your last name : ')
    #Return both names.
    return first,last

def password(first,last):
    d = len(last)//2
    if len(last) % 2 == 0 :
        print('password : ',first[:3:]+last[d-2:d+1])
    else :
        print('password : ',first[:3:]+last[d-1:d+2])

def password2(first,last):
    d = len(last)//2
    if len(last) % 2 == 0 :
        pas = first[:3:]+last[d-2:d+1]
    else :
        pas = first[:3:]+last[d-1:d+2]
    return 'password : ' + pas 
    

    
main()
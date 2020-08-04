hours = int(input('Enter the number of hours worked: '))
rate = int(input('Enter the hourly pay rate: '))


if hours > 40:
    ohour = hours-40
    pay = 40*rate
    pay2 = (rate*1.5)*ohour+pay
    print('the gross pay is $',pay2)
else :
    pay = hours*rate 
    print('The gross pay is $',pay)




    

#This program calculates sales commissions.
# Create a variable to control the loop.
keep_going = 'y'

# Calculate  a series of commissions.
while keep_going == 'y' or keep_going == 'Y' :
    #Get a salesperson's sales and sommission rate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    #Ca
    commission = sales * comm_rate

    print('The commmission is $',\
        format(commission, ',.2f'), sep='')

    keep_going = input('Do you want to calculate another' +  \
        ' commission (Enter y or Y for yes): ')

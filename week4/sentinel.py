item = 'y'


while item == 'y' or item == 'Y':
    wholesale = float(input("Enter the item's wholesale cost : "))
    price = wholesale * 2.5

    print("Retail price :" ,\
        format (price,',.2f'))

    item = input("Do you have another item ?" +\
    "(Enter Y or y for yes ) :")


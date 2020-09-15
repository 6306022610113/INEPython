def main():
    num_day = int(input("For how many days do " +\
                        "you have sales? "))

    sales_file = open('week7/sales.txt','w')

    for count in range(1, num_day + 1):
        sales = float(input('Enter the sales for day #' + \
                            str(count) + ': '))
        
        sales_file.write(str(sales) + '\n')

    sales_file.close()
    print('Data written to sales.txt')

main()

    
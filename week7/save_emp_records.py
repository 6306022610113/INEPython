def main():
    #get the number of employee records to create.
    num_emps = int(input('How many employee records' + \
                        'do you want to create? '))
    
    emp_file = open('week7/employees.txt','w')

    for count in range(1, num_emps + 1):

        print('Enter dete for employees #' , count, sep='')
        name = input('Name: ') 
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.write('Name: ',name + '\n')
        emp_file.write('ID: ',id_num + '\n')
        emp_file.write('Department: ',dept + '\n')

        print()

    emp_file.close()
    print('Employees records written to employees.txt')

main()

show_name_all = 1
add_name = 2
delete_name = 3
end = 4

def main():
    choice = 0
    try:
        while choice != end:
            show_menu()
            choice = int(input('Enter your choice : '))
            if choice == show_name_all:
                infile = open('week7/nameclass.txt','r')
                r = infile.read()
                infile.close()
                print(r)
            elif choice == add_name:
                infile = open('week7/nameclass.txt','a')
                infile.write('\n'+(str(input(' Enter your name: '))))
                infile.close()
                print('your data add list')
            elif choice == delete_name:
                infile = open('week7/nameclass.txt','r')
                r = infile.read()
                for count in r:
                    g += 1 
                
                infile.close()

            elif choice == end :
                print('Exiting the program...')
            else:
                print('Error : invalid selection.')
    except Exception as err:
        print(err)

           
def show_menu():
    print('         MENU')
    print('1) Show Name All')
    print('2) Add Name')
    print('3) Delete Name')
    print('4) Quit')

main()
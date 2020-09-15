def main():
    #Open a file named philosophers.txt
    outfile = open('philosophers.txt','w')

    outfile.write('John Locke\n')
    outfile.write('David Hum\n')
    outfile.write('Edmund Burke\n')

    outfile.close()

main()
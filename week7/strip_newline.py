def main():

    infile = open('philosophers.txt','r')

    #read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #String the \n from each string.
    line1 = line1.rsplit('\n')
    line2 = line2.rsplit('\n')
    line3 = line3.rsplit('\n')

    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()
def main():

    infile = open('week7/philosophers.txt','r')

    #read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()
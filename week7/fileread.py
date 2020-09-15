def main():

    infile = open('philosophers.txt','r')

    file_contents = infile.read()

    infile.close()

    #print the data that was read into
    #memory
    print(file_contents)

main()
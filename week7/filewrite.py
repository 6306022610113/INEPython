def main():
    #Open a file named philosophers.txt
    outfile = open('week7/philosophers.txt','w')

    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    outfile.close()

main()
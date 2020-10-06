def main():
    cities = ['New York','\nBoston','\nAtlanta','\nDallas']

    outfile = open('week8/cities.txt','w')
    outfile.writelines(cities)
    outfile.close()

main()
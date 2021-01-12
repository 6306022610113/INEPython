def main():
    lstn = input("YOUR LIST : ")
    list = [lstn.split(",")]
    print(lstn)
    for i in range(len(lstn)-1,0,-1):
        for j in range(i):
            if lstn[j]>lstn[j+1]:
                tmp = lstn[j]
                lstn[j] = lstn[j+1]
                lstn[j+1] = tmp
                print(lstn)
            

                

main()
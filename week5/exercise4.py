str1 = "English = 78 Science = 83 Math = 68 History = 65 art = 78"
print(str1.split())
separatewords = str1.split()
sum = 0
k = 0
for i in separatewords:
    if i.isnumeric():
        sum = sum + int(i)
        k = k + 1
print("sum is : ",sum)
print("Average is :",sum/k)


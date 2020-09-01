male = int(input('Input number of male students: '))
female = int(input('Input number of female students: '))
sum = male + female
sum1 = male/sum*100
sum2 = female/sum*100
print('There are %d students with %.2f male and %.2f famale'%(sum,sum1,sum2))

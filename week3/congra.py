test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))
ave = (test1+test2+test3)/3
print('The average score is',ave)

if ave > 95:
    print('Congratulations!')
    print('That is a great average!')
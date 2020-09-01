
keep = 'y'

while keep == 'Y' or keep == 'y':
    tf = input('Select topiglatin(T) or Frompiglatin(F) : ')
    sen = input('Input sentence: ')

    if tf == 'T' :
        print("Results traslation :".join(topiglatin(sen)))
    elif tf == 'F' :
        print("Results traslation :".join(frompiglatin(sen)))
    else :
        print("ERROR")

    keep = print("Any more sentence Y(yes) or N(no) :")

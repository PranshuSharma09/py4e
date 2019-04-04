diction = dict()
a = input("enter file name: ")
try:
    file = open(a)
    for line in file:
        words = line.split()
        for word in words:
            diction[word] = diction.get(word,0) + 1
    while True:
        x = input("Enter a word: ")
        if x == "end program" or x == "End Program":
            print('Thank You')
            break
        elif x in diction:
            print('true', diction.get(x))
            continue
        else:
            print('false', diction.get(x,0))
            continue
except:
    print('file does not exist')

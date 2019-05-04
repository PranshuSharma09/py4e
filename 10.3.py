import string
count = 0
diction = dict()
a = input("enter file name: ")
try:
    file = open(a)
except:
    print('file does not exist')
    exit()
for line in file:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            count += 1
            if letter not in diction:
                diction[letter] = 1
            else:
                diction[letter] += 1
lst = list()
for k,v in list(diction.items()):
    lst.append((v/count*100,k))
lst.sort(reverse=True)
for k,v in lst:
    print(k,v)

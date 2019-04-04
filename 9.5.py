diction = dict()
a = input("enter file name: ")
try:
    file = open(a)
except:
    print('file does not exist')
    exit()
for line in file:
    words = line.split()
    if len(words) == 0 or len(words) < 1 or words[0] != 'From':
        continue
    else:
        w = words[1].find('@')
        word = words[1][w+1:]
        if word not in diction:
            diction[word] = 1
        else:
            diction[word] += 1
print(diction)

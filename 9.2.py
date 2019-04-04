diction = dict()
a = input("enter file name: ")
try:
    file = open(a)
except:
    print('file does not exist')
    exit()
for line in file:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[2] not in diction:
            diction[words[2]] = 1
        else:
            diction[words[2]] += 1
print(diction)

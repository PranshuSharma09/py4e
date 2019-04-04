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
        if words[1] not in diction:
            diction[words[1]] = 1
        else:
            diction[words[1]] += 1
print(diction)

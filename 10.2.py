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
        w = words[5].find(':')
        word = words[5][:w]
        if word not in diction:
            diction[word] = 1
        else:
            diction[word] += 1
lst = list()
#print(sorted([(v,k) for k,v in diction.items()])) **can be used in place of following lines**
for k,v in list(diction.items()):
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print(k,v)

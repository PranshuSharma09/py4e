x = input('enter file name: ')
di = dict()
try:
    fhand = open(x)
except:
    print('file does not exist.')
    quit()
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': continue
    else:
        if words[1] not in di:
            di[words[1]] = 1
        else:
            di[words[1]] += 1
lst = list()
for (k,v) in list(di.items()):
    lst.append((v,k))
lst.sort(reverse=True)
for v,k in lst[:1]:
    print(k,v)

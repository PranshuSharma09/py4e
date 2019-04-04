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
        if words[1] not in diction:
            diction[words[1]] = 1
        else:
            diction[words[1]] += 1
largest = 0
for word in diction:
    if diction[word] > largest:
        largest = diction[word]
        largest_word = word
print(largest_word, largest)

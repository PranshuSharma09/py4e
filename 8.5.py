x = input('enter file name: ')
count = 0
try:
    fhand = open(x)
except:
    print('file does not exist.')
    quit()
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': continue
    count = count + 1
    print (words[1])
print('there were',count,'lines in the file with From as the first word')

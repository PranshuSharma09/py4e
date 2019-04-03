x = input('enter file name')
y = open(x)
c = 0
for line in y:
    if line.startswith('Subject'):
        c = c + 1
print(c)

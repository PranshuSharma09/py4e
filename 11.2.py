import re
count = 0
a = input("enter file name: ")
try:
    file = open(a)
except:
    print('file does not exist')
    exit()
z = []
for line in file:
    line = line.rstrip()
    x = re.findall('^New.+: ([0-9.]+)', line)
    if x != []:
        count += 1
        for y in x:
            y = float(y)
            z = z + [y]
ysum = sum(z)
avg = ysum/count
print(avg)

import re
count = 0
a = input("enter file name: ")
try:
    file = open(a)
except:
    print('file does not exist')
    exit()
re_exp = input ('Enter a Regular expression: ')
for line in file:
    line = line.rstrip()
    x = re.findall(re_exp, line)
    if len(x) > 0:
        count += 1
print('file had', count ,'lines that matched', re_exp)

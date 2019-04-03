x = input("enter file name: ")
try:
    y = open(x)
except:
    print("file does not exist")
    quit()
z = 0
c = 0
for line in y:
    if line.startswith('X-DSPAM-Confidence:'):
        d = line.find('0')
        s = line[d:]
        c = c + 1
        z = z + float(s)
print('Avg spam confidence:', z/c)

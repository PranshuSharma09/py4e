newlist = []
x = input("enter file name: ")
try:
    fhand = open(x)
    for line in fhand :
        words = line.split()
        for word in words:
            if word not in newlist:
                 newlist.append(word)
    print(sorted(newlist))
except:
    print("file does not exist.")

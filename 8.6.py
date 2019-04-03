newlist = []
while True:
    x = input("Enter a number: ")
    if x == "done" or x == "Done":
        break
    try:
        x = float(x)
    except:
        print ("Not a number")
        exit()
    newlist.append(x)
print("Maximum: ", max(newlist))
print("Minimum: ", min(newlist))

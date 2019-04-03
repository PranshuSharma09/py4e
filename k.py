count = 0
total = 0
while True:
    x = input('enter a number: ')
    if x == 'done':
        break
    try:
        x = float(x)
    except:
        print("bad data")
        continue
    count = count + 1
    total = total + x
    avg = total/count
print(total, count, avg)

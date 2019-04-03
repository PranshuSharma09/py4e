a=input('enter hours:')
b=input('enter rate:')
a=float(a)
b=float(b)
if a>40:
    z=a-40
    d=b*1.5
    e=(40*b)+(z*d)
    print('pay=', e)
else:
    c=(a)*(b)
    print('pay=',c)

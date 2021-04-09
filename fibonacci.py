limit = int(input('Enter limit: '))
fl = []

def fib():
    for x in range(limit):
        if x==0 or  x==1:
            fl.append(x)
        else:
            a = fl[x-1]            
            b =fl[x-2]            
            fl.append(a+b)

fib()
print(fl)

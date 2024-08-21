import math
math.pi
def greet(name):
    print("Hello, "+name+ "!")
    print("john")   #output:Hello john!

def fibo(n):
    a = [0,1]
    for i in range(2,n):
        sum = a[i-1] + a[i-2]
        a.append(sum)
    return a
print(fibo(6))
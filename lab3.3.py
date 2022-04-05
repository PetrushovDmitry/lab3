import math
def f(x):
    return math.cos(x)-2-x
eps = 0.0001
a = float(input())
b = float(input())
e = 1.0
c = 0.0
x = 0.0
lastx=0.0
while e >eps:
    c = (a+b)/2
    C = f(a)
    B = (f(c)-f(a))/(c-a)+((f(b)-f(c))/(b-c)-(f(c)-f(a))/(c-a))/(b-a)*(a-c)
    A = ((f(b)-f(c))/(b-c)-(f(c)-f(a))/(c-a))/(b-a)
    if B*B-4*A*C < 0:
        print("на данном промежутке корней нет")
        break
    x1 = a - 2*C/(B+math.sqrt(B*B-4*A*C))
    x2 = a - 2*C/(B-math.sqrt(B*B-4*A*C))
    if ((a <=x1) and (b >= x1))or ((a >= x1) and (b <= x1)):
        x = x1
    elif ((a <=x2) and (b >= x2)) or ((a >= x2) and (b <= x2)):
        x = x2
    if f(a)*f(x) < 0:
        b = x
    elif f(b)*f(x) <0:
        a=x
    e = abs(lastx-x)
    lastx = x
print(x)
    

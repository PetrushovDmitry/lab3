import math
eps = 0.5*pow(10,(-4))
def f(x):
    return x - math.cos(math.sqrt(math.pow(x,2)+1))
def df(x):
    return 1 + math.sin(math.sqrt(math.pow(x,2)+1))*x/math.sqrt(math.pow(x,2)+1)
x = (1+0)/2.0
dx = 1.0

while abs(dx) > eps:
    dx = f(x)/df(x)
    x = x-dx
print(x)           

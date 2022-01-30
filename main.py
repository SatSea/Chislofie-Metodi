import math

# input 
a = float(input()) # lower interval
b = float(input()) # higher interval
e = float(input()) # accuracy


#def for func
def f(x):
 return math.exp(-x)-(math.sin(x)**2)/2


def half_division_method(a,b,e):
    x=a
    while ((b-a) > e):

        x = (a+b)/2

        if (f(x) == 0):
            break

        if (f(x)*f(a) < 0):
            b = x
        else:
            a = x
            
print("Корень равен: {x}", half_division_method(a,b,e))




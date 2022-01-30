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


#отделение корней
def root_separation(a,b,e):
    aVal=f(a)
    bVal=f(b)
    if (aVal>0 and bVal<0) or (aVal<0 and bVal>0):
        return Method(b,a,e)
    else:
        print("Что-то пошло не так")
        return 1


print("Корень равен: {x}", root_separation(a,b,e))




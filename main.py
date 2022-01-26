import math

# input 
a = float(input())
b = float(input())
e = float(input())


#def for func
def f(x):
 return math.exp(-x)-(math.sin(x)**2)/2


x=a
while ((b-a) > e):

    x = (a+b)/2

    if (f(x) == 0):
        break

    if (f(x)*f(a) < 0):
        b = x
    else:
        a = x
            
print("Корень равен: {x}", x)

print(x)



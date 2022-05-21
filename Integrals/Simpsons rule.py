import math

def simpson(f, a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,int(n/2 + 1)):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)

def function(x): return math.cos(x)-12*(x**3)

print(simpson(function, 0.0, math.pi, 6))
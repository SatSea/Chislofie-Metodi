import math

#функция
def f(x):
    return math.exp(-x)-(math.sin(x)**2)/2
 

#производная
def f1(x):
    return -(math.exp(-x))-math.sin(2*x)/2

#производная второго порядка
def f2(x):
    return math.exp(x)-math.cos(2*x)

def Method(x1, x2, e):
    try:
        x1  = x0 - fx(x0) / dfx(x0); 
        while (abs(x1 - x0) > e):
            x0 = x1
            x1 = x0 - fx(x0) / dfx(x0)
    except ValueError:
        print("Значение не получилось")


# a=float(input())
# b=float(input())
# e=float(input())
a = -2
b = 5
e = 0.5

def root_separation(a,b,e):
    count = 0
    x1 = a
    x2 = x1 + e
    y1 = f(x1)
    while(x2 < b):
        y2 = f(x2)
        if (y1 * y2 <= 0):
            print(x1,x2)
            Method(x1,x2,0.0001)
            count += 1
        x1 = x2
        x2 = x1 + e
        y1 = y2
    print(f"Поиск завершен\nНайдено {count} корней")

root_separation(a,b,e)


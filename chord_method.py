import math

global otvet
otvet = ""

# функция
def f(x):
    return math.exp(-x)-(math.sin(x)**2)/2


# производная
def f1(x):
    return -(math.exp(-x))-math.sin(2*x)/2

# производная второго порядка
def f2(x):
    return math.exp(x)-math.cos(2*x)


def Method(x0, e):
    try:
        global otvet
        x = x0 - f(x0) / f1(x0)
        while (abs(x - x0) > e):
            x0 = x
            x = x0 - f(x0) / f1(x0)
        otvet += ("Корень равен: %.3f\n" % x)

    except ValueError:
        print("Значение не получилось")

a = -2
b = 5
e = 0.5

def root_separation(a, b, e):
    count = 0
    x1 = a
    x2 = x1 + e
    y1 = f(x1)
    while(x2 < b):
        y2 = f(x2)
        if (y1 * y2 <= 0):
            # print(x1, x2)
            # print(f(x1)*f2(x1))
            # print(f(x2)*f2(x2))
            count += 1
            if (f(x2)* f2(x2) > 0):
                Method(x1, 0.0001)
            else:
               Method(x2, 0.0001) 
        x1 = x2
        x2 = x1 + e
        y1 = y2
    print(f"Поиск завершен\nНайдено {count} корней\n" + otvet[:-2])


# a=float(input())
# b=float(input())
# e=float(input())
root_separation(a, b, e)

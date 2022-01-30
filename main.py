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
    count = 0
    try:
        x1 = a
        x2 = x1 + e
        y1 = f(x1)
        while(x2 < b):
            y2 = f(x2)
            if (y1 * y2 <= 0):
                half_division_metho(a,b,0.0001)
                count += 1
            x1 = x2
            x2 = x1 + e
            y1 = y2
        print(f"Поиск завершен\nНайдено {count} корней")
    except:
        print("Что-то пошло не так" )


print("Корень равен: {x}", root_separation(a,b,e))




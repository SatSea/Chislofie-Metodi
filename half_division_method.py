import math

global otvet
otvet = ""

# input 
a = float(input()) # lower interval
b = float(input()) # higher interval
e = float(input()) # accuracy


#def for func
def f(x):
 return math.exp(-x)-(math.sin(x)**2)/2


def half_division_method(a,b,e):
    x=a
    global otvet
    while ((b-a) > e):
        x = (a+b)/2
        if (f(x) == 0):
            break
        if (f(x)*f(a) < 0):
            b = x
        else:
            a = x
    
    otvet += ("Корень равен: %.3f\n" % x)   


#отделение корней
def root_separation(a,b,h):
    count = 0
    try:
        x1 = a
        x2 = x1 + h
        y1 = f(x1)
        while(x2 < b):
            y2 = f(x2)
            if (y1 * y2 <= 0):
                print(x1)
                print(x2)
                half_division_method(x1,x2,0.0001)
                count += 1
            x1 = x2
            x2 = x1 + h
            y1 = y2
        print(f"Поиск завершен\nНайдено {count} корней\n" + otvet[:-1])
    except:
        print("Что-то пошло не так" )


root_separation(a,b,e)
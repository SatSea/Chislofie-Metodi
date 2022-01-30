import math

# input 
a = float(input()) # lower interval
b = float(input()) # higher interval
e = float(input()) # accuracy

#функция
def f(x):
    return math.exp(-x)-(math.sin(x)**2)/2
 

#производная
def f1(x):
    return -(math.exp(-x))-math.sin(2*x)/2


#сам метод
def Method(a,b,e):
    x0=(a+b)/2 
    xn=f(x0)
    xn1=xn-f(xn)/f1(xn)
    while abs(xn1-xn)>e:
        xn=xn1 
        xn1=xn-f(xn)/f1(xn)
    print(f"Найден корень %.4f с погрешностью {e}" % xn1)


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
                Method(a,b,0.0001)
                count += 1
            x1 = x2
            x2 = x1 + e
            y1 = y2
        print(f"Поиск завершен\nНайдено {count} корней")
    except:
        print("Что-то пошло не так" )

root_separation(a,b,e)
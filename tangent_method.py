import math

global otvet
otvet = ""

# input 
# a = float(input()) # lower interval
# b = float(input()) # higher interval
# e = float(input()) # accuracy

a = -2
b = 5
e = 0.5

#функция
def f(x):
    return math.exp(-x)-(math.sin(x)**2)/2
 

#производная
def f1(x):
    return -(math.exp(-x))-math.sin(2*x)/2


#сам метод
def Method(a,b,e):
    while(abs(b - a) > e):
        a = b - (b - a) * f(b) / (f(b) - f(a))
        b = a - (a - b) * f(a) / (f(a) - f(b))
    otvet += ("Корень равен: %.3f\n" % x)


#отделение корней
def root_separation(a,b,e):
    count = 0
    x1 = a
    x2 = x1 + e
    y1 = f(x1)
    while(x2 < b):
        y2 = f(x2)
        if (y1 * y2 <= 0):
            print(str(a)+" "+str(b))
            Method(x1,x2,0.0001)
            count += 1
        x1 = x2
        x2 = x1 + e
        y1 = y2
    print(f"Поиск завершен\nНайдено {count} корней\n" + otvet[:-2])

root_separation(a,b,e)
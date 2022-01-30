import math


#функция
def F(x):
    return 0.1*math.pow(x,2)-x*math.log(x)
 

#производная
def F1(x):
    return 0.2*x-math.log(x)-1


#сам метод
def Method(a,b,e):
    x0=(a+b)/2 
    xn=F(x0)
    xn1=xn-F(xn)/F1(xn)
    while abs(xn1-xn)>e:
        xn=xn1 
        xn1=xn-F(xn)/F1(xn)
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

print("Корень равен: {x}", root_separation(a,b,e))
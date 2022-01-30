import math
import numpy as np


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
    return xn1


#отделение корней
def root_separation(a,b,e):
    try:
        interval = np.linspace(a, b, e)
        for x in interval:
            if f(x) * f(y) > 0: # если на отрезке нет корня, смотрим следующий
                Method(a,b,e)
    except:
        print("Что-то пошло не так {}", )

print("Корень равен: {x}", root_separation(a,b,e))
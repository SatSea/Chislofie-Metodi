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
    return xn1


#отделение корней
def root_separation(a,b,e):
    aVal=f(a)
    bVal=f(b)
    if (aVal>0 and bVal<0) or (aVal<0 and bVal>0):
        return Method(b,a,e)
    else:
        return 0
import math



#функция
def F(x):
    return 0.1*math.pow(x,2)-x*math.log(x)
 
#производная
def F1(x):
    return 0.2*x-math.log(x)-1
 
 
def Method(a,b):
    x0=(a+b)/2
    xn=F(x0)
    xn1=xn-F(xn)/F1(xn)
    while abs(xn1-xn)>math.pow(10,-5):
        xn=xn1 
        xn1=xn-F(xn)/F1(xn)
    return xn1

def Get_root():
    a = input()
    b = input()
    h = input()

    x1 = a
    x2 = x1 + h
    y1 = f(x1)

    while(x2<b):
        y2 = f(x2)
        if (y1*y2 =< 0):
            print(x1, x2)
        x1 = x2
        x2 = x1+h
        y1=y2


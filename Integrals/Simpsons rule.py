import math

def simpson(a, b, n):
    h=(b-a)/(n-1)
    k=0.0
    x=a + h
    if(n%2==0):
        while(x<b):
            k += 2*function(x)
            x += 2*h

        x = a + 2*h
        while(x<b):
            k += 4*function(x)
            x += 2*h
    else:
        while(x<b):
            k += 4*function(x)
            x += 2*h

        x = a + 2*h
        while(x<b):
            k += 2*function(x)
            x += 2*h
    print(f"Функция а {function(a)} Функция б {function(b)}")
    return (h/3)*(function(a)+function(b)+k)

def function(x): return math.cos(x)-12*(x**3)

def main():
    a = float(input("Введите нижний интервал: "))
    b = float(input("Введите верхний интервал: "))
    n = float(input("Введите количество точек: "))
    print(simpson(a,b,(b-a)/(n-1)))

if(__name__ == "__main__"):
    main()

'''
def simpson_easy(a,b):
    return ((b-a)/6)*(function(a)+function(b)+4*function((a+b)/2))
'''
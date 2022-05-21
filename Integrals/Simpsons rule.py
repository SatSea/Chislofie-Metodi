import math

def simpson(a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,int(n/2 + 1)):
        k += 4*function(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*function(x)
        x += 2*h
    return (h/3)*(function(a)+function(b)+k)

def function(x): return math.cos(x)-12*(x**3)

def main():
    a = float(input("Введите нижний интервал: "))
    b = float(input("Введите верхний интервал: "))
    n = float(input("Введите количество точек: "))
    print(simpson(a,b,(b-a)/(n-1)))

if(__name__ == "__main__"):
    main()

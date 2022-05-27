import math

def simpson(a, b, n):
    h=(b-a)/(n)
    k=0.0
    x= a + 2*h
    if(n%2==0):
        while(x<=b-h):
            k += 2*function(x)
            x += 2*h

        x = a + h 
        while(x<=b-h):
            k += 4*function(x)
            x += 2*h
    else:
        while(x<=b-h):
            k += 4*function(x)
            x += 2*h

        x = a + h 
        while(x<=b-h):
            k += 2*function(x)
            x += 2*h
    res = (h/3)*(function(a)+function(b)+k)
    print(f"Ответ по методу Симпсона равен: {res}")
    return res

def function(x): return math.cos(x)-12*(x**3)

def main():
    simpson(float(input("Введите нижний интервал: ")),float(input("Введите верхний интервал: ")),float(input("Введите количество точек: ")))


if(__name__ == "__main__"):
    main()

'''
def simpson_easy(a,b):
    return ((b-a)/6)*(function(a)+function(b)+4*function((a+b)/2))
'''
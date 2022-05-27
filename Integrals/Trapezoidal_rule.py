import math
 
def trap(a,b,n):
    h=(b-a)/(n)
    s=0.5*(function(a)+function(b))
    x=a+h
    while (x<=b-h):
        s+=function(x)
        x+=h
    res = h*s
    print(f"Ответ по методу трапеции равен: {res}")
    return res
    
def function(x):
    return math.cos(x)-12*(x**3)

def main():
    trap(float(input("Введите нижний интервал: ")),float(input("Введите верхний интервал: ")),float(input("Введите количество точек: ")))

if(__name__ == "__main__"):
    main()
import math
 
def trap(a,b,h):
    s=0.5*(function(a)+function(b))
    x=a+h
    while (x<=b-h):
        s+=function(x)
        x+=h
    return h*s
    
def function(x):
    return math.cos(x)-12*(x**3)

def main():
    a = float(input("Введите нижний интервал: "))
    b = float(input("Введите верхний интервал: "))
    n = float(input("Введите количество точек: "))
    print("Ответ равен: " + str(trap(a,b,(b-a)/(n-1))))

if(__name__ == "__main__"):
    main()
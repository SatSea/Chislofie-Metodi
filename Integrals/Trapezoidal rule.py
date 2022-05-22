import math
 
def trap(a,b,n):
    h=(b-a)/(n-1)
    s=0.5*(function(a)+function(b))
    x=a+h
    while (x<b):
        s+=function(x)
        x+=h
    return h*s
    
def function(x):
    return math.cos(x)-12*(x**3)

def main():
   print("Ответ равен: " + str(trap(float(input("Введите нижний интервал: ")),float(input("Введите верхний интервал: ")),float(input("Введите количество точек: ")))))

if(__name__ == "__main__"):
    main()
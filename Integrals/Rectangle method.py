import math

def function(x): return math.cos(x)-12*(x**3)

def rect(a,b,h):
    i=a
    sumL, sumR = 0,0
    while(i<b):
        sumL += function(i)
        i+=h
    i=a+h
    while(i<=b):
        sumR += function(i)
        i+=h
    resL = sumL*h
    resR = sumR*h
    print(f"По левому прямоугольнику: {resL} \n По правому прямоугольнику: {resR}")
    
def main():
    a = float(input("Введите нижний интервал: "))
    b = float(input("Введите верхний интервал: "))
    n = float(input("Введите количество точек: "))
    rect(a,b,(b-a)/(n-1))

if(__name__ == "__main__"):
    main()
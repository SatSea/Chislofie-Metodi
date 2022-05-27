import math

def function(x): return math.cos(x)-12*(x**3)

def rect(a,b,n):
    h=(b-a)/(n)
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
    print(f"По левому прямоугольнику: {resL}\nПо правому прямоугольнику: {resR}")
    return [resL,resR]
    
def main():
    rect(float(input("Введите нижний интервал: ")),float(input("Введите верхний интервал: ")),float(input("Введите количество точек: ")))


if(__name__ == "__main__"):
    main()
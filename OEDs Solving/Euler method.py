def Euler(n, h, x, y):
    for i in range(int(n)):
        y += h * f(x, y)
        x += h
        print(f"x: {x} y: {y}")
    return x, y 

def f(x, y):
    return y/(1+x) #

def main():
    print("Введите нижний интервал:")
    x1 = float(input())
    print("Введите верхний интервал:")
    x2 = float(input())
    print("Введите шаг:")
    h = float(input())
    n = (x2-x1)/h
    print(Euler(n,h,x1,x2))

if (__name__=="__main__"):
    main()
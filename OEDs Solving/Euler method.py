def Euler(n, h, x, y, y0):
    yi = y0/(1+x)
    hY = h* yi
    print(f"|| 1 || {x:.3f} || {yi:.3f} ||")
    yi = yi + hY
    x += h
    print(f"|| 1 || {x:.3f} || {yi:.3f} ||")
    for i in range(int(n-1)):
        ydif = yi/(1+x)
        hY = h* ydif
        yi = ydif + hY
        x += h
        print(f"|| {i+2} || {x:.3f} || {yi:.3f} ||")

def f(x, y):
    return y/(1+x)

def main():
    print("Введите нижний интервал:")
    x1 = float(input())
    print("Введите верхний интервал:")
    x2 = float(input())
    print("Введите шаг:")
    h = float(input())
    print("Введите y0:")
    y0 = float(input())
    n = (x2-x1)/h
    print("Ответ равен:")
    print("_________________________")
    print("|| n ||   x   ||   y   ||")
    print("||---||-------||-------||")
    Euler(n,h,x1,x2,y0)
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

if (__name__=="__main__"):
    main()
from Trapezoidal_rule import trap
from Simpsons_rule import simpson
from Rectangle_method import rect

def main():
    a = 0
    b = 3.14
    n = 6
    trap(a,b,n)
    simpson(a,b,n)
    rect(a,b,n)

if(__name__ == "__main__"):
    main()
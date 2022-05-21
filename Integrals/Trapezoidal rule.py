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

def test(): 
    print("Ответ равен: "+str(trap(0,math.pi,0.0001)))

test()
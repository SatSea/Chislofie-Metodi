def Matrix (): 
    matrix = [] 
    matrix = input().split()
    for i in range(len(matrix)):
        matrix[i]=float(matrix[i])
    return matrix
    
def lagrange(x,y,xs):
    xi = [0,0,0,0]
    xj = [0,0,0,0]
    A = [0,0,0,0]
    Xi= [0,0,0,0]
    
    xi[0]=xs-x[0]
    xi[1]=xs-x[1]
    xi[2]=xs-x[2]
    xi[3]=xs-x[3]
    
    xj[0]= (x[0]-x[1]) * (x[0]-x[2]) * (x[0]-x[3])
    xj[1]= (x[1]-x[0]) * (x[1]-x[2]) * (x[1]-x[3])
    xj[2]= (x[2]-x[0]) * (x[2]-x[1]) * (x[2]-x[3])
    xj[3]= (x[3]-x[0]) * (x[3]-x[1]) * (x[3]-x[2])
    
    Xi[0] = xi[1] * xi[2] * xi[3]
    Xi[1] = xi[0] * xi[2] * xi[3]
    Xi[2] = xi[0] * xi[1] * xi[3]
    Xi[3] = xi[0] * xi[1] * xi[2]
    
    A[0] = Xi[0]/xj[0]
    A[1] = Xi[1]/xj[1]
    A[2] = Xi[2]/xj[2]
    A[3] = Xi[3]/xj[3]
    print(f"A1={A[0]} A1={A[1]}=A2 {A[2]} A3={A[3]}")
    otvet = y[0]*A[0]+y[1]*A[1]+y[2]*A[2]+y[3]*A[3]
    print(otvet)

def main():
    print("Введите x")
    x = Matrix()
    print("Введите y")
    y = Matrix()
    xs = float(input("Введите x*"))
    lagrange(x,y,xs)


if (__name__=="__main__"):
    main()
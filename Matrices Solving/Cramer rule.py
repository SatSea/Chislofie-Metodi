def divider(matrix):
    global matrix1
    global matrix2
    matrix2=[]
    matrix1=matrix
    for line in range(len(matrix1)):
        matrix2.append(matrix1[line][len(matrix1[line])-1])
        matrix1[line].pop(len(matrix1[line])-1)
    #for line in range(len(matrix1)):
        #print(str(matrix1[line]) + ' ' + str(matrix2[line]))

def Cramer():
    definer = matrix1[0][0]*matrix1[1][1]*matrix1[2][2]+matrix1[0][1]*matrix1[1][2]*matrix1[2][0]+matrix1[0][2]*matrix1[1][0]*matrix1[2][1]-matrix1[0][2]*matrix1[1][1]*matrix1[2][0]-matrix1[0][1]*matrix1[1][0]*matrix1[2][2]-matrix1[0][0]*matrix1[1][2]*matrix1[2][1]
    if(definer == 0):
        print("Нельзя найти ответ, так как определитель равен 0")
        return None
    definer1 = matrix2[0]*matrix1[1][1]*matrix1[2][2]+matrix1[0][1]*matrix1[1][2]*matrix2[2]+matrix1[0][2]*matrix2[1]*matrix1[2][1]-matrix1[0][2]*matrix1[1][1]*matrix2[2]-matrix1[0][1]*matrix2[1]*matrix1[2][2]-matrix2[0]*matrix1[1][2]*matrix1[2][1]
    definer2 = matrix1[0][0]*matrix2[1]*matrix1[2][2]+matrix2[0]*matrix1[1][2]*matrix1[2][0]+matrix1[0][2]*matrix1[1][0]*matrix2[2]-matrix1[0][2]*matrix2[1]*matrix1[2][0]-matrix2[0]*matrix1[1][0]*matrix1[2][2]-matrix1[0][0]*matrix1[1][2]*matrix2[2]
    definer3 = matrix1[0][0]*matrix1[1][1]*matrix2[2]+matrix1[0][1]*matrix2[1]*matrix1[2][0]+matrix2[0]*matrix1[1][0]*matrix1[2][1]-matrix2[0]*matrix1[1][1]*matrix1[2][0]-matrix1[0][1]*matrix1[1][0]*matrix2[2]-matrix1[0][0]*matrix2[1]*matrix1[2][1]

    x1=definer1/definer
    x2=definer2/definer
    x3=definer3/definer
    print("Ответ равен: x1=%.3f, x2=%.3f, x3=%.3f" % (x1,x2,x3))
    reply = [x1,x2,x3]
    return reply
    

def Matrix ( x,y ): 
    matrix = [] 
    for x in range(x): 
        matrix.append([int(y) for y in input().split()])
    return matrix

def main():
    print("Введите матрицу")
    #matrix = Matrix(3,3)
    #matrix = [[1,-4,-2,-3],[3,1,1,5],[3,-5,-6,-9]]
    matrix = [[2,3,-1,4],[1,1,3,5],[3,-4,1,0]]
    divider(matrix)
    Cramer()


if (__name__=="__main__"):
    main()
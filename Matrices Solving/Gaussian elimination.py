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
    Gauss()

def SwapRows (row1, row2):
    matrix1[row1], matrix1[row2] = matrix1[row2], matrix1[row1]
    matrix2[row1], matrix2[row2] = matrix2[row2], matrix2[row1]

def DivideRow (row, divider):
    matrix1[row] = [a / divider for a in matrix1[row]]
    matrix2[row] /= divider

def CombineRows (row, source_row, weight):
    matrix1[row] = [(a + k * weight) for a,k in zip(matrix1[row], matrix1[source_row])]
    matrix2[row] += matrix2[source_row] * weight

def Gauss():
    for column in range(len(matrix1)):
        current_row = None
        for r in range(column, len(matrix1)):
            if current_row is None or abs(matrix1[r][column]) > abs(matrix1[current_row][column]):
                current_row = r
        if current_row is None:
            print ("решений нет")
            return None
        if current_row != column:
            SwapRows (current_row, column)
        DivideRow (column, matrix1[column][column])
        for r in range(column+1, len(matrix1)):
            CombineRows(r, column, -matrix1[r][column])
    #for line in range(len(matrix1)):
        #print(matrix1[line],matrix2[line])
    X = [0 for b in matrix2]
    for i in range(len(matrix2)-1, -1, -1):
        X[i] = matrix2[i] - sum(x*a for x,a in zip(X[(i+1):], matrix1[i][(i+1):]))
   
    print("Получили ответ:")
    print( "\n".join("X{0} =\t{1:6.2f}".format(i+1,x) for i,x in enumerate(X)) )
    

def Matrix ( x,y ):
    print("Введите матрицу")
    matrix = [] 
    for x in range(x): 
        matrix.append([int(y) for y in input().split()])
    return matrix

def main():
    #matrix = Matrix(3,3)
    matrix = [[1,-4,-2,-3],[3,1,1,5],[3,-5,-6,-9]]
    divider(matrix)


if (__name__=="__main__"):
    main()

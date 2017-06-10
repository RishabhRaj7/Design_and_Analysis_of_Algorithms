def new_m(p, q):
    matrix = [[0 for row in range(p)] for col in range(q)]
    return matrix

def input_m(matrix, r, c):
    print("Enter elements of the matrix:")
    for i in range(r):
        for j in range(c):
            matrix[i][j] = int(input())
    return matrix

def matrix_m(a, b):
    if len(a[0]) != len(b):
        return "Matrices do not satisfy the condition m*n and n*p"
    else:
        matrix = new_m(len(a), len(b[0]))
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    matrix[i][j] += a[i][k]*b[k][j]
    return matrix

def split_m(matrix):
    a = matrix
    b = matrix
    c = matrix
    d = matrix
    while(len(a) > len(matrix)/2):
        a = a[:len(a)/2]
        b = b[:len(b)/2]
        c = c[len(c)/2:]
        d = d[len(d)/2:]
    while(len(a[0]) > len(matrix[0])/2):
        for i in range(len(a[0])/2):
            a[i] = a[i][:len(a[i])/2]
            b[i] = b[i][len(b[i])/2:]
            c[i] = c[i][:len(c[i])/2]
            d[i] = d[i][len(d[i])/2:]
    return a,b,c,d

def add_m(a, b):
    if type(a) == int:
        d = a + b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] + b[i][j])
            d.append(c)
    return d

def sub_m(a, b):
    if type(a) == int:
        d = a - b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] - b[i][j])
            d.append(c)
    return d

def strassen_m(a, b, q):
    if q == 1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]
        return d
    else:
        a11, a12, a21, a22 = split_m(a)
        b11, b12, b21, b22 = split_m(b)

        # p1 = a11 * (b12-b22)
        p1 = strassen_m(a11, sub_m(b12,b22), q/2)

        # p2 = (a11+a12) * b22
        p2 = strassen_m(add_m(a11,a12), b22, q/2)

        # p3 = (a21+a22) * b11
        p3 = strassen_m(add_m(a21,a22), b11, q/2)

        # p4 = a22 * (b21-b11)
        p4 = strassen_m(a22, sub_m(b21,b11), q/2)

        # p5 = (a11+a22) * (b11+b22)
        p5 = strassen_m(add_m(a11,a22), add_m(b11,b22), q/2)

        # p6 = (a12-a22) * (b21+b22)
        p6 = strassen_m(sub_m(a12,a22), add_m(b21,b22), q/2)

        # p7 = (a11-a21) * (b11+b12)
        p7 = strassen_m(sub_m(a11,a21), add_m(b11,b12), q/2)

        # c11 = p5 + p4 - p2 + p6
        c11 = add_m(sub_m(add_m(p5, p4), p2), p6)

        # c12 = p1 + p2
        c12 = add_m(p1, p2)

        # c21 = p3 + p4
        c21 = add_m(p3, p4)

        # c22 = p1 + p5 - p3 - p7
        c22 = sub_m(sub_m(add_m(p1, p5), p3), p7)

        c = new_m(len(c11)*2,len(c11)*2)
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j]                   = c11[i][j]
                c[i][j+len(c11)]          = c12[i][j]
                c[i+len(c11)][j]          = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c

print ("Enter rows and columns of first matrix:")
r1 = int(input())
c1 = int(input())
matrixA = new_m(r1, c1)
matrixA = input_m(matrixA, r1, c1)

print ("Enter rows and columns of second matrix:")
r2 = int(input())
c2 = int(input())
matrixB = new_m(r2, c2)
matrixB = input_m(matrixB, r2, c2)

if r1==c1==r2==c2:
    print ("Product of Matrices:")
    print strassen_m(matrixA, matrixB, r1)
else:
    print matrix_m(matrixA, matrixB)

m = int(input("Enter the number of Row in Matrix1: "))
n = int(input("Enter the number of Column in Matrix1: "))

Mat1 = []
for i in range(0,m):
    Mat1.append([])
for i in range(0,m):
    for j in range(0,n):
        Mat1[i].append(j)
        Mat1[i][j]=0
        print("Entry in row: ",i+1," column: ",j+1)
        Mat1[i][j] = int(input())
print(Mat1)

p = int(input("Enter the number of Row in Matrix2: "))
q = int(input("Enter the number of Column in Matrix2: "))

Mat2 = []
for i in range(0,p):
    Mat2.append([])
for i in range(0,p):
    for j in range(0,q):
        Mat2[i].append(j)
        Mat2[i][j]=0
        print("Entry in row: ",i+1," column: ",j+1)
        Mat2[i][j] = int(input())
print(Mat2)

Res = []
for i in range(0,m):
    Res.append([])
for i in range(0,m):
    for j in range(0,q):
        Res[i].append(j)
        Res[i][j] = 0
for p in range(len(Mat1)):
    for q in range(len(Mat2[0])):
        for r in range(len(Mat2[0])):
            Res[p][q] += Mat1[p][r] * Mat2[r][q]
print(Res)

    

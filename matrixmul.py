#matrix multiplication

X = [[24,17,3],
    [44 ,5,6],
    [74 ,8,29]]
Y = [[15,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(X)):
   
   for j in range(len(Y[0])):
       
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

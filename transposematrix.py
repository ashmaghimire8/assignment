


X = [[12,7,1],
    [4 ,5,8],
    [3 ,8,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

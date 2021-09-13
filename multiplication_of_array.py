import numpy as np 

a=np.array([[1,2,3],[4,5,6]],dtype=int)
b=np.array([[2,3,4],[5,6,7]],dtype=int)
c=np.array([[0,0,0],[0,0,0]],dtype=int)
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
print(c)


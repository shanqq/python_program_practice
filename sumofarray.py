import numpy as np 

a=np.array([[1,2,3],[4,5,6]],dtype=int)
b=np.array([[2,3,4],[5,6,7]],dtype=int)
sum1=0
c=np.array([[0,0,0],[0,0,0]],dtype=int)
for i in range(len(a)):
    for j in range(len(b)):
        sum1+=b[i][j]+a[i][j]
print(sum1,end=" ")



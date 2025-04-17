#Lab7-Write a python program to solve Matrix Chain Multiplication Problem using Dynamic Programming

import numpy as np
def MatrixChain(p):
  n=len(p)
  for i in range(1,n):
    m[i][i]=0
  for l in range(2,n):
    for i in range(1,n-l+1):
      j=i+l-1
      m[i][j]=999999
      for k in range (i,j):
        c= m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
        if c < m[i][j]:
          m[i][j] = c
          s[i][j] = k
#Driver Code
n=int(input("Enter Number of Matrices:"))
shape = (n+1, n+1)
m = np.zeros(shape)
s = np.zeros(shape)
p=[]
print("Enter Matrix Order Array")
for i in range(n+1):
  p.append(int(input()))
n=len(p)
MatrixChain(p)
print("M Matrix:")
print(m)
print("S Matrix")
print(s)
print("Minimum Number of Steps Required=",m[1][n-1])

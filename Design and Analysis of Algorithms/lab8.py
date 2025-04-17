#Lab8- Write a python program to implement 0/1 Khanpsack Problem using Dynamic Programming

import numpy as np
def ZeroOneKnapsack(w,v,KW,n):
  for wt in range(KW+1):
    c[0][wt]=0
  for i in range(n+1):
    c[i][0]=0
  for i in range(1,n+1):
    for wt in range (1,KW+1):
      if(w[i]<=wt): 
       c[i][wt]= max(v[i]+c[i-1][wt-w[i]], c[i-1][wt])
      else:
        c[i][wt]=c[i-1][wt];
  return c

#Driver Code
n=int(input("Enter Number of Items:"))
KW=int(input("Enter Capacity of Knapsack:"))
shape = (n+1, KW+1)
c = np.zeros(shape)
w=[]
v=[]
w.append(0)#Dummy Data, weighst are stored from index 1
v.append(0)#Dummy Data, values are stored from index 1
print("Enter weights:")
for i in range(n):
  w.append(int(input()))
print("Enter values:")
for i in range(n):
  v.append(int(input()))
ZeroOneKnapsack(w,v,KW,n)
print("Profit Matrix:")
print(c)
print("Max Profit that can be Earned:",c[n][w])

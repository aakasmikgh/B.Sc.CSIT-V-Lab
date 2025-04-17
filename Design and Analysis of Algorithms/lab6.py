#lab-6: Write a python program to implement Job Sequencing with deadlines Problem

def jobsequencing(x,d,p,n):
  s=[]
  for i in range(max(d)+1):
    s.append(0)
  for i in range(n):
    deadline=d[i]
    k=deadline
    while(k>=1):
      if(s[k]==0):
        s[k]=x[i]
        break
      k=k-1
  return s
def swap(a,i,j):
  temp=a[i]
  a[i]=a[j]
  a[j]=temp
 
#Driver code
x=[]
p=[]
d=[]
n=int(input("Enter no. of jobs:"))
for i in range(n):
  x.append(i+1)
print("Enter Deadlines:")
for i in range(n):
  d.append(int(input()))
print("Enter Profits:")
for i in range(n):
  p.append(int(input()))
#Soring jobs on the basis of profit
for i in range(n-1):
  for j in range(n-1):
    if(p[j]<p[j+1]):
      swap(p,j,j+1)
      swap(d,j,j+1)
      swap(x,j,j+1)
print("After Sorting:")
print("x=",x)
print("d=",d)
print("p=",p)
s=jobsequencing(x,d,p,n)
print("Solution:",s[1:])
 
 
#Profit Calculation
profit=0
for i in range(0,max(d)):
  profit=profit+p[i]
print("Profit=",profit)
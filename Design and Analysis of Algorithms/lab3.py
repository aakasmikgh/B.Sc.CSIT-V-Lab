msteps=0
qsteps=0
def mergesort(a, l, r):
  global msteps
  if(l<r): #if dataset has more than 1 data
    m=(int)((l+r)/2)
    mergesort(a,l,m)
    mergesort(a,m+1,r)
    merge(a,l,m,r)
    msteps=msteps+5
  msteps=msteps+1
def merge(a,l,m,r):
  global msteps
  i=k=l
  j=m+1
  msteps=msteps+2
  while(i<=m and j<=r):
    if(a[i]<a[j]):
      b[k]=a[i]
      i=i+1
      k=k+1
      msteps=msteps+6
    else:
      b[k]=a[j]
      k=k+1
      j=j+1
      msteps=msteps+6
  while(i<=m):
    b[k]=a[i]
    k=k+1
    i=i+1
    msteps=msteps+4
  while(j<=r):
    b[k]=a[j]
    k=k+1
    j=j+1
    msteps=msteps+4
  for i in range (l,r+1):
    a[i]=b[i]
    msteps=msteps+3
  msteps=msteps+2
 
 
def quicksort(c,l,r):
  global qsteps
  if(l<r):
    p=partition(c,l,r)
    quicksort(c,l,p-1)
    quicksort(c,p+1,r)
    qsteps=qsteps+4
  qsteps=qsteps+1
def partition(c,l,r):
  global qsteps
  pivot=c[l]
  x=l
  y=r
  qsteps=qsteps+3
  while(x<y):#while x and y are not crossed
    while(c[x]<=pivot):
      x=x+1
      qsteps=qsteps+4
      if(x>r):
        break
    while(c[y]>pivot):
      y=y-1
      qsteps=qsteps+3
    if(x<y):#x and y not crossed
      swap(c,x,y)
      qsteps=qsteps+2
    qsteps=qsteps+1
  swap(c,y,l)#x and y are crossed
  qsteps=qsteps+1
  return y
def swap(c,i,j):
  global qsteps
  temp=c[i]
  c[i]=c[j]
  c[j]=temp
  qsteps=qsteps+3
 
#Driver Code
import random
n = int (input("enter n:"))
a = []
c=[]
for i in  range(n):
  e=random.randint(0,n)
  a.append(e)
  c.append(e)
b = [None]*n
mergesort(a,0,n-1)
print("Sorted data (mergesort)",a)
print("#Steps(MergeSort)=",msteps)
quicksort(c,0,n-1)
print("Sorted data (quicksort)",c)
print("#Steps(QuickSort)=",qsteps)

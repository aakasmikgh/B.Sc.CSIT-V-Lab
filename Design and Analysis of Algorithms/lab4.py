import random
msteps=0
hsteps=0
def mergesort(a, l, r):
  global msteps
  if(l<r):
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
      msteps=msteps+5
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
 
def heapsort(c,n):
  global hsteps
  buildheap(c,n)
  i=n
  hsteps=hsteps+2
  while(i>=1):
    swap(c,1,n)
    n=n-1
    heapify(c,n,1)
    i=i-1
    hsteps=hsteps+5
  hsteps=hsteps+1
def buildheap(c,n):
  global hsteps
  i=(int)(n/2)
  hsteps=hsteps+1
  while(i>=1):
    heapify(c,n,i)
    i=i-1
    hsteps=hsteps+3
  hsteps=hsteps+1
def heapify(c,n,i):
  global hsteps
  l=2*i
  r=2*i+1
  largest=i
  hsteps=hsteps+3
  if(l<=n and c[l]>c[largest]):
    largest=l
    hsteps=hsteps+3
  hsteps=hsteps+2
  if(r<=n and c[r]>c[largest]):
    largest=r
    hsteps=hsteps+3
  hsteps=hsteps+2
  if(largest!=i):
    swap(c,i,largest)
    heapify(c,n,largest)
    hsteps=hsteps+3
  hsteps=hsteps+1
def swap(a,i,j):
  global hsteps
  temp=a[i]
  a[i]=a[j]
  a[j]=temp
  hsteps=hsteps+3
 
#Driver Code
n = int (input("enter n:"))
a = []
c=[]
c.append(None)
for i in  range(n):
  e=random.randint(0,n)
  a.append(e)
  c.append(e)
b=[None]*n
mergesort(a,0,n-1)
print("Sorted data (mergesort)",a)
print("#Steps(mergesort)=",msteps)
heapsort(c,n)
print("Sorted data (heapsort)",c[1:n+1])
print("#Steps(heapsort)=",hsteps)
#Lab 4
import random
msteps=0
hsteps=0
def mergesort(a, l, r):
  global msteps
  if(l<r):
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
      msteps=msteps+5
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
 
def heapsort(c,n):
  global hsteps
  buildheap(c,n)
  i=n
  hsteps=hsteps+2
  while(i>=1):
    swap(c,1,n)
    n=n-1
    heapify(c,n,1)
    i=i-1
    hsteps=hsteps+5
  hsteps=hsteps+1
def buildheap(c,n):
  global hsteps
  i=(int)(n/2)
  hsteps=hsteps+1
  while(i>=1):
    heapify(c,n,i)
    i=i-1
    hsteps=hsteps+3
  hsteps=hsteps+1
def heapify(c,n,i):
  global hsteps
  l=2*i
  r=2*i+1
  largest=i
  hsteps=hsteps+3
  if(l<=n and c[l]>c[largest]):
    largest=l
    hsteps=hsteps+3
  hsteps=hsteps+2
  if(r<=n and c[r]>c[largest]):
    largest=r
    hsteps=hsteps+3
  hsteps=hsteps+2
  if(largest!=i):
    swap(c,i,largest)
    heapify(c,n,largest)
    hsteps=hsteps+3
  hsteps=hsteps+1
def swap(a,i,j):
  global hsteps
  temp=a[i]
  a[i]=a[j]
  a[j]=temp
  hsteps=hsteps+3
 
#Driver Code
n = int (input("enter n:"))
a = []
c=[]
c.append(None)
for i in  range(n):
  e=random.randint(0,n)
  a.append(e)
  c.append(e)
b=[None]*n
mergesort(a,0,n-1)
print("Sorted data (mergesort)",a)
print("#Steps(mergesort)=",msteps)
heapsort(c,n)
print("Sorted data (heapsort)",c[1:n+1])
print("#Steps(heapsort)=",hsteps)
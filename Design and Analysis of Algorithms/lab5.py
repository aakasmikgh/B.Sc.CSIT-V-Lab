def fractionalknapsack(w,v,W,n):
  s=[]
  for i in range(n):
    s.append(0)
  remw=W
  for i in range(n):
    if(w[i]<=remw):
      s[i]=1
      remw=remw-w[i]
    else:
      s[i]=remw/w[i]
      break  
  return s
def swap(a,i,j):
  temp=a[i]
  a[i]=a[j]
  a[j]=temp
 
#Driver code
w=[]
v=[]
n=int(input("Enter no. of Items:"))
W=int(input("Enter Capacity of Knapsack:"))
print("Enter Item weights:")
for i in range(n):
  w.append(int(input()))
print("Enter Item Values:")
for i in range(n):
  v.append(int(input()))
ratio=[]
for i in range(n):
  ratio.append(v[i]/w[i])
for i in range(n-1):
  for j in range(n-1):
    if(ratio[j]<ratio[j+1]):
      swap(ratio,j,j+1)
      swap(v,j,j+1)
      swap(w,j,j+1)
print("After Sorting:")
print("vi/wi=",ratio)
print("Value Array=",v)
print("Weight Array=",w)
s=fractionalknapsack(w,v,W,n)
print("Solution:",s)
profit=0
for i in range(n):
  profit=profit+s[i]*v[i]
print("Profit=",profit)
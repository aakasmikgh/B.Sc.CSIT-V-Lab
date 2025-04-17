#Lab9-Write a python program to implement subset sum problem using Backtracking

def findsum(s):
  sum=0
  for x in s:
    sum=sum+x
  return sum

def subsetsum(s,subset,targetsum,i,n):
  sum=findsum(subset)
  if(sum==targetsum):
    print("Solution:",subset)
    return
  elif(i==n):
    return
  else:
    if(sum>targetsum):
      return
    else:
      subset.append(s[i])
      #print("Include ", s[i])
      #print(subset)
      subsetsum(s,subset,targetsum,i+1,n)
      subset.pop()
      #print("Exclude ", s[i])
      #print(subset)
      subsetsum(s,subset,targetsum,i+1,n)

#Driver Code
s=[]
subset=[]
n=int(input("Enter Number of Set Elements:"))
print("Enter Set Elements:")
for i in range(n):
  s.append(int(input()))
targetsum=int(input("Enter Target Sum:"))
subsetsum(s,subset,targetsum,0,n)
#Lab 1: Empirical Analysis of Bubble Sort and Selection Sort
def bubblesort(a,n):
  steps=0
  for i in range (1,n):#no of passes
    for j in range (n-i):
      if (a[j+1] < a[j]):
        temp = a[j+1]
        a[j+1]=a[j]
        a[j]=temp
        steps=steps+6
      steps=steps+3
    steps=steps+2
  print("No of steps(Bubble Sort)",steps)
def selectionsort(b,n):
  steps=0
  for i in range (0,n-1):#no of passes
    min = b[i]
    mi=i
    steps=steps+4
    for j in range (i+1,n):# finds min
      if(b[j]<min):
        min = b[j]
        mi = j
        steps=steps+5
      steps=steps+3
    temp=b[i]
    b[i]= b[mi]
    b[mi] = temp
    steps=steps+3
  print("No of steps(Selection Sort)",steps)
 
# Driver Code
import random
n = int (input("Enter n:"))
a = []
b= []
for i in  range(n):
  e=random.randint(0,n)
  a.append(e)
  b.append(e)
 
bubblesort(a,n)
print("Sorted data (bubble)",a)
selectionsort(b,n)
print("Sorted data (selection)",b)
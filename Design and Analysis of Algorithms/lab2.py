# Emphirical analysis of selection sort and insertion sort
# a. write down functions
# b. generate n random numbers and store them in two lists
# c. sort the array of random number using both sorting algorithms
# d. count and display number of steps taken by both sorting algorithms
# e. repeat above process process for n=10 to 100 in interval by 10.
 



def insertionsort(a,n):
  steps=0
  for i in range (1,n):#no of passes
    key=a[i]
    j=i-1
    steps=steps+4
    while j>=0 and key<a[j]:
      a[j+1]=a[j]
      j=j-1
      steps=steps+4
    a[j+1]=key
    steps=steps+1
  print("No of steps(Insertion Sort)",steps)
 
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
 
insertionsort(a,n)
print("Sorted data (insertion)",a)
selectionsort(b,n)
print("Sorted data (selection)",b)
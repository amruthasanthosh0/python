import array as arr
def insertionsort(x):
   for i in range(1,len(x)):
      key=x[i]
      j=i-1
      while j>=0 and key<x[j]:
         x[j+1]=x[j]
         j-=1
      x[j+1]=key
   return x
array=arr.array('i',[])
n=int(input("enter the number of elements in the array"))
print("enter the elements")
for i in range(0,n):
  ele=int(input())
  array.insert(i,ele)
print(f" the sorted array is {insertionsort(array)}")

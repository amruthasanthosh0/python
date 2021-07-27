import array as arr
def bubblesort(x):
   for i in range(0,len(x)):
      for j in range(0,len(x)-1-i):
         if x[j]>x[j+1]:
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp
   return x

array=arr.array('i',[])
n=int(input("enter the number of elements in the array"))
print("enter the elements")
for i in range(0,n):
  ele=int(input())
  array.insert(i,ele)
print(f" the sorted array is {bubblesort(array)}")

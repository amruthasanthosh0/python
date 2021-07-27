import array as arr
def matching(x):
   for i in range(0,len(x)):
      for j in range(i+1,len(x)):
         if x[i]==x[j]:
            print ( x[i])
      

array=arr.array('i',[])
n=int(input("enter the number of elements: "))
for i in range (0,n):
   ele=int(input())
   array.insert(i,ele)
print("the matching elements are: ")
matching(array)


import array as arr
def sumofarray(x):
   sum=0;
   for i in x:
      sum=sum+i
   return sum
array=arr.array('i',[])
n=int(input("enter the number of elements: "))
for i in range (0,n):
   ele=int(input())
   array.insert(i,ele)
print(f"""the sum of array is : {sumofarray(array)}""")


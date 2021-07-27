import array as arr
import numpy as np
def secondlarge(x):
   x=np.sort(x)
   return x[len(x)-2]
array=arr.array('i',[])
n=int(input("enter the number of elements: "))
for i in range (0,n):
   ele=int(input())
   array.insert(i,ele)
print(f"""the second largest number of  array is : {secondlarge(array)}""")

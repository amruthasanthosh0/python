import array as arr
def binarysearch(arrray,key):
   low,high=0,len(array)
   mid=int((low+high)/2)
   while(low<=high):
      if(array[mid]==key):
         return (f"the element is present at the index {mid}")
         break;
      elif(array[mid]<key):
         low=mid+1
      elif(array[mid]>key):
         high=mid-1
      mid=int((low+high)/2)
   if(low>high):
      return ("The element is not found")
      
array=arr.array('i',[])
n=int(input("enter the number of elements in the array"))
print("enter the elements")
for i in range(0,n):
  ele=int(input())
  array.insert(i,ele)
key=int(input("enter the key to search"))
print(binarysearch(array,key))
  
   

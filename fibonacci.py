def fib(n):   #using reccursion
   if n<=1:
      return (n)
   else:
      return (fib(n-1)+fib(n-2))
   
   
   
def fibb(n):
   n1,n2=0,1
   if n==1:
      print (n1)
   else:
      for i in range(0,n):
         print(n1)
         nth=n1+n2
         n1=n2
         n2=nth
      
x=int(input("Enter how many terms :"))
print ("The fibonacci series is :")
fibb(x)

print ("The fibonacci series using reccursion is :")
for i in range(x):
   print(fib(i))


def isprime(x):
   if (x==0 | x==1):
   	return False
   elif x==2:
        return True
   else:
        for i in range (2,int(x/2)):
           if x%i==0:
              return False
        return True
        
n=int(input("enter the number: "))
p=isprime(n)
if p==True:
   print(f""" {n} is a prime number""")
else:
   print(f""" {n} is not a prime number""")

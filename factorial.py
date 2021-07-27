def fact(n):
   if n==1:
      return n
   else:
      return (n*fact(n-1))
      
x=int(input("Enter the number :"))
print (f"""The factorial {x} is {fact(x)} """)

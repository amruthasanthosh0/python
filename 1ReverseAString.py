def strreverse(x): #simple method
  return x[::-1]
  
def reverse(x): #using for loop
  rev=""
  for i in x  :
     rev=i+rev
  return rev
    
  
  
str=input ("Enter a string:")

print (f"""the reverse of string is :{reverse(str)}""")

print (f"""the reverse of string is :{strreverse(str)}""")





def charcount(x):
  count=0
  for i in x  :
     if i!= " " :
        count+=1
  return count
    
  
  
str=input ("Enter a string:")

print (f"""the number of characters in string is :{charcount(str)}""")


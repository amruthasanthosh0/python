def charcount(x):
  vowel=0
  cons=0
  x=x.lower()
  for i in x  :
     if i in ['a','e','i','o','u']:
        vowel+=1
     elif i !=' ':
        cons+=1
  return (cons,vowel)
    
  
  
str=input ("Enter a string:")
a,b=charcount(str)

print (f"""the number of vowels in string is :{b}""")
print (f"""the number of consonants in string is :{a}""")

def strreverse(x): #simple method
  return x[::-1]
  
str1=input ("Enter first string :")
str2=input ("Enter second string :")
if str1== strreverse(str2):
   print("these strings are panagram")
else:
   print("these strings are not panagrams")




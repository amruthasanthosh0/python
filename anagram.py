str1=input ("Enter first string :")
str2=input ("Enter second string :")
if len(str1)== len(str2):
   str1=sorted(str1)
   str2=sorted(str2)
   if str1 == str2:
      print("these strings are panagram")
else:
   print("these strings are not panagrams")


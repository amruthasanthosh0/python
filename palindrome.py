def palindrome(x):
  if x[::-1]==x:
     return (f"""{x} is a palindrome""")
  else:
     return(f"""{x} is not a palindrome""")
     
string=input("enter the string: ")
print (palindrome(string))

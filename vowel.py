import string
n=input()
list1=['A','E','I','O','U','a','e','i','o','u']
list2=list(string.ascii_uppercase)+list(string.ascii_lowercase)
if n in list2:
  if n in list1:
    print("Vowel")
  else:
    print("Consonent")
else:
  print("Invalid")

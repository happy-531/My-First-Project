def check(psk):
   for password in psk:
    if password.isupper():
     global upperc
     upperc=True
    if password.islower():
     global lowerc
     lowerc=True
    if password.isdigit():
     global numc
     numc=True
    if len(psk) > 8:
      global lengthc
      lengthc=True
    if not password.isalnum():
     global symbolc
     symbolc=True

   result=upperc + lowerc + numc + lengthc + symbolc
   if upperc:
    print("uppercase :✅")
   if lowerc:
    print("lowercase :✅")
   if numc:
    print("number : ✅")
   if lengthc:
    print("length :✅")
   if symbolc:
    print("alnum :✅")

   if result == 5:
    print("Your password is very strong.")
   elif result ==4:
    print("Your password is strong.")
   elif result ==3:
    print("Your password is medium.")
   elif result <3:
    print("Your password is weak")

exit=True
while exit:
 print("\nPassword Strength Checker enter 0 to shut down the program\n")
 try:
  psk=input("Enter your password:")
 except KeyboardInterrupt:
  print("ERROR!")

 upperc=False
 lowerc=False
 numc=False
 lengthc=False
 symbolc=False

 if psk=="0":
  print("exitting...")
  exit=False
 else:
  check(psk)

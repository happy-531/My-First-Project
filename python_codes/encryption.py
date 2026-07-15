import random
def code(message):
 coded=[]
 for m in message:
  if len(m)>=3:
   random_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@","#","&","$"]
   letter1=m[0]
   str1=m[1:]+letter1
   coded_message="".join(random.sample(random_list,3))+str1+"".join(random.sample(random_list,3))
  elif len(m)>0:
   list1=[letter for letter in m]
   list1.reverse()
   coded_message="".join(list1)

  coded.append(coded_message)

 return " ".join(coded)
def decode(message):
 decoded=[]
 for m in message:
  if len(m)>=3:
   str1=m[3:-3]
   a=list(str1)
   l1=a.pop()
   decoded_message=l1+"".join(a)
  elif len(m)>0:
   list1=[letter for letter in m]
   list1.reverse()
   decoded_message="".join(list1)

  decoded.append(decoded_message)

 return " ".join(decoded)

def ui():
 user_want=input("Select the number of what you want :\n1. code\n2. decode or Type `exit` to exit\n>").strip()
 if user_want=="1":
  message=input("Enter the message: ").strip().split(" ")
  coded_message=code(message) if message else print("No message found")
  play_again=input(f"Your code message is : {coded_message}\nDo you want to use more (1 for yes 0 for no):").strip()
  if play_again=="1":
   ui()
 elif user_want=="2":
  message=input("Enter the message: ").strip().split(" ")
  decoded_message=decode(message) if message else print("No message found")
  play_again=input(f"Your code message is : {decoded_message}\nDo you want to use more (1 for yes 0 for no):").strip()
  if play_again=="1":
   ui()
 elif user_want.lower()=="exit":
  return
 else:
  print("\ninvalid input !\n\n")
  ui()

ui()

import datetime
import os

try:
 action=int(input("what do you want to know ?\n[1] date or time\n[2] location of directory\n[3] Create a folder\n[4] List of directories\n"))

 match action:
  case 1:
   now=datetime.datetime.now()
   print(now.strftime("Time : %H:%M\ndate : %d %b %Y"))
  case 2:
   print(os.getcwd())
  case 3:
   try:
    name=input("enter the name of the folder you want to create :")
    os.mkdir(name)
    print("Directory created successfully\n")
    path=os.path.join(os.getcwd(), name)
    print(path)
   except FileNotFoundError:
    print("Inavlid name")
   except FileExistsError:
    print("file already exist")
  case 4:
   list=os.listdir()
   print("\n"+"-"*30)
   print(*list,sep="\n")
  case _:
   print("error 404 !\nplease enter valid number")

except ValueError:
 print("error 404 !\nplease enter valid number")

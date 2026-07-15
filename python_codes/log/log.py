import getpass, os
name=input("Enter the username :")
password=getpass.getpass("Enter password:")

date = os.popen("date").read().strip()

with open("logs.txt","a") as a:
 log=f"\n{date}|{name}|{password}\n"
 a.write(log)
print("saved")

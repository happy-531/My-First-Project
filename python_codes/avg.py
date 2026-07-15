def avg(n1,n2,n3):
 try:
  list = [float(n1), float(n2), float(n3)]
  avg = round( sum(list) / len(list) , 3)
  print(f"\nThe average number of {int(n1)}, {int(n2)} and {int(n3)} is :{avg}\n")

 except ValueError:
  print("\nInvalid input\n")

"""
def avg(n1,n2,n3):
 list1 = [n1,n2,n3]
 if n1.isdigit() and n2.isdigit() and n3.isdigit():
  list = [float(n1),float(n2),float(n3)]
  avg = round( sum(list)/len(list) ,3)
  print(f"\nThe average number of {int(n1)}, {int(n2)} and {int(n3)} is :{avg}\n")
 else:
  print("\nInvalid input\n")
"""
limit=0
while True:

 if limit == 33:
  print("\n[*]Alert:\n-Your limit is reached!\n-Try to run the code again if you want to use more.")
  break

 n1 = input("Enter the first number : ").lower().strip()
 if "exit" in n1:
  break
 n2 = input("Enter the second number : ").lower().strip()
 if "exit" in n2:
  break
 n3 = input("Enter the third number : ").lower().strip()
 if "exit" in n3:
  break

 avg(n1,n2,n3)

 limit += 1

print("\nClosing the program...")
print("Thank you!\n")

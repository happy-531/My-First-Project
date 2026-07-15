from random import randint

# Game function
def game(you):
 choice = dict[you]
 you = choice

 # Normal computer
 computer = randint(0,2)

 # Unbeatable computer
 """
 if choice == 1:
  computer = 0
 elif choice == 0:
  computer = 2
 elif choice == 2:
  computer = 1
 """
 # Result
 print(f"\nComputer choice:{rdict[computer]}\nYour choice :{rdict[you]}")
 if you!=computer:
  if computer == 0 and you == 1:
   print("you lose !")
  elif computer == 0 and you == 2:
   print("you won !")
  elif computer == 1 and you == 0:
   print("you Won !")
  elif computer == 1 and you == 2:
   print("you lose !")
  elif computer == 2 and you == 0:
   print("you lose !")
  elif computer == 2 and you == 1:
   print("you Won !")
 else:
  print("Its a draw")


# Dictonaries
dict = {
"rock":1,
"paper":0,
"scissor":2,
"scissors":2,
"r":1,
"p":0,
"s":2
}

rdict = {
1:"rock",
0:"paper",
2:"scissor"
}

# Game loop
while True:
 print("-"*30)
 you1 = input("\nSelect Rock, Paper or Scissor: ").lower().strip()
 options = ["rock","paper","scissor","scissors","r","p","s"]

 if you1 in options:
  game(you1)
 elif you1=="exit":
  break
 else:
  print("Invalid choice!")

print("Exiting...")
print("Thank you!")

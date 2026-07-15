import random
num=random.randrange(1,100)
l=10
def check():
    admn=input("-----Are you the admin ? type 0 for yes and 1 for no: ").lower().strip()
    if admn=="0" or "y" in admn:
        admin=True
        passa="7890"
        chk=input("----Enter password to confirm you are admin:").lower().strip()
        if chk==passa:
            admin=True
            print(f"-----you are admin\n ----welcome \n\n-------The number is {num}.\n\n")
            
        else:
            print("---!!! incorrect password you are not admin !!!")
            admin=False
    else:
        admin=False
    
check()

a=0
while 1==1:
    guess=int(input(f"---Guess the number between 1 to 100 you have {l} attempts :"))

    if guess>100 or guess<1:
        print("--Alert!!! \n -***The number must be between 1 to 100.***")
        continue 
    
    a+=1
    l-=1
    
    if guess==num:
        print(f"-Congratulations 👏 🎉,\nYou guessed it correct 💯 in {a} attempts.")
        break
    elif guess>num:
        print(f"-----your number is higher.\n Now you have {l} attempts left.")
    elif guess<num:
        print(f"-----your number lower.\n ----Now you have {l} attempts left.")
    if l==0:
        print("!!!!! you have reached the maximum attempts limit. !!!!!")
        break

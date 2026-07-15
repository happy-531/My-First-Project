def check(username,password):
 database={
 "happy":12345678,
 "harshit":"harshit07",
 "God":"godzilla"
 }

 if (username in database and password==database[username]):
  return True
 else:
  return False

if __name__ == "__main__":
 username=input("Enter your username: ").strip()
 password=input("Enter your password: ").strip()

 if check(username,password):
  print("ACCESS GRANTED !\n You are welcome \n link: https://secret.cracker.lovable.app")
 else:
  print("ACCESS DENIED , please try entering correct username and password")

import socket
while True:
 start=input("Do you want to start the dns lookup ? (yes/no): ").strip()
 if start.lower()=="yes":
  domain=input("Enter the domain of the website: ")
  ip=socket.gethostbyname(domain)
  print(f"Ip address: {ip}")
 elif start.lower()=="no":
  print("Exiting the program")
  exit()
 else:
  print("invalid input")

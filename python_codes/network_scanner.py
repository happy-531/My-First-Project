import socket

def scan(ip,type):
 ports=[21,22,80,443,3306,8022,8080]
 common_ports = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8022: "SSH"
 }

 open_ports=[]
 if type == "basic":
  for port in ports:
   print(f"Trying the port {port}")
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   s.settimeout(0.5)

   connect = s.connect_ex((ip,port))

   if connect == 0:
    print(f"OPEN PORT FOUND : {port}")
    service = common_ports.get(port,"Service is not in our dictionary")
    open_ports.append(f"Ports : {port} is open | Service : {service}")

   s.close()
  return open_ports
 else:
  for port in range(1,10000+1):
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   s.settimeout(0.19)

   connect = s.connect_ex((ip,port))

   if connect == 0:
    print(f"OPEN PORT FOUND : {port}")
    service = common_ports.get(port,"Service is not in our dictionary")
    open_ports.append(f"Ports : {port} is open | Service : {service}")

   s.close()
  return open_ports

target_ip = input("Enter the target ip: ")
port_scan_type= input("Enter the type : (u for ultimate port scanner (10,000 ports) or just enter for basic scan) : ").lower().strip()

if target_ip:
 if port_scan_type == "u":
  scan_result = scan(target_ip,"ultimate")
 else:
  scan_result = scan(target_ip,"basic")

 if scan_result:
  print(*scan_result,sep="\n")
 else:
  print("No open ports found\n")
else:
 print("Invalid ip !\n")

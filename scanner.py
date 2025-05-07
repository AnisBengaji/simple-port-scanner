import socket


target= input("enter the desired ip adress: ")


ports= [21,22,23,25,53,80,110,135,139,443,445,8080]

print(f"\nScanning {target}...\n")


for port in ports:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)
    result = sock.connect_ex((target,port))
    if result == 0:
        print(f"[+] port {port} IS OPEN")
        sock.close()

print("\nSCAN complete.")


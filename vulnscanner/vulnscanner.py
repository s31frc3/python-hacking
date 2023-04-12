import portscanner

targets_ip = input('[+] enter target to scan for vulnerable open ports: ')
port_number = int(input('Enter amount of ports to scan: '))
vul_file = input('enter path to the file with vulnerable softwares: ')
print('\n')

target = portscanner.port_scan(targets_ip, port_number)
target.scan()
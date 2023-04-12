import portscanner

targets_ip = input('[+] enter target to scan for vulnerable open ports: ')
port_number = int(input('Enter amount of ports to scan: '))
vul_file = input('enter path to the file with vulnerable softwares: ')
print('\n')

target = portscanner.port_scan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0) #from beginning
        for line in file.readlines():
            if line.strip() in banner:
                print(f'[!] vulnerable banner: {banner} on port {str(target.open_ports[count])}')
    count += 1
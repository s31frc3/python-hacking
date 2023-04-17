import hashlib
from termcolor import colored

type_of_hash = str(input(colored('which type of hash u want to bruteforce? ', 'blue')))
file_path = str(input(colored('enter path to dictionary file to bruteforce with: ', 'blue')))
hash_to_decrypt = str(input(colored('enter hash value to bluteforce: ', 'blue')))

with open(file_path, 'r', encoding='latin1') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(colored(f'found md5 password: {line.strip()}', 'green'))
                exit(0)
        if type_of_hash == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(colored(f'found md5 password: {line.strip()}', 'green'))
                exit(0)
    print(colored('password not in file', 'red'))
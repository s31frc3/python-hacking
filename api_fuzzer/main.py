import requests, sys

# usage: $ cat fuzz_dirs.txt | python3 main.py

def loop():
    for word in sys.stdin:
        res = requests.get(url = f"http://10.10.163.14/{word}")
        if res.status_code == 404:
            loop()
        else:
            data =res.text
            print(res)
            print(word)
            print(data)

loop()
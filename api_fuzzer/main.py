import requests, sys

# fuzz_url = "https://lootdog.io/api/face/promos/?format=json&lang=EN"

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
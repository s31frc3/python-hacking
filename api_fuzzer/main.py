import requests, sys

fuzz_url = "http://10.10.163.14/robots.txt"

res = requests.get(url=fuzz_url)

print(res)
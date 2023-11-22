import requests, sys
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup) # same as curl
    # print(soup.find("a"))  # find all <a> tag
    # print(soup.find_all("id=asdf"))  # find all id=asdf in page
    tag = soup.find_all('a')
    for t in tag:
        url2 = t.get("href")
        print(url2)

url = sys.stdin.readline().strip()
get_page(url)
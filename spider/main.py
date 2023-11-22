import requests, sys
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    # print(soup.find_all("a"))  # find all <a> tags
    # print(soup.find_all("id=asdf"))  # find all id=asdf in page

url = sys.stdin.readline().strip()
get_page(url)
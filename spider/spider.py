import requests, sys, threading
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib import *
import argparse

visited_urls = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        # print(urls)

        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url, urls2)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass


parser = argparse.ArgumentParser(description='Process some arguments.')
parser.add_argument('-u', '--url', help='URL argument')
parser.add_argument('-k', '--keyword', help='Keyword argument')
args = parser.parse_args()
url = args.url
keyword = args.keyword

array = [threading.Thread(target=spider_urls(url, keyword)).start() for x in range(1000)]
import requests
from bs4 import BeautifulSoup

def get_xkdc(url):
    response = requests.get(url)
    max_downloads = 4 

    if response.status_code != requests.codes.ok:
        print("Error occured: " ,response.status_code)
        return 

    html = response.text
    soup = BeautifulSoup(html, "lxml")
    print(soup.prettify)

get_xkdc("https://xkcd.com/")
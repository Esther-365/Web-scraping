#Right now PyPi is blocking my requests and I don't know what to do at my level, so I'm going to come back to this project.
from bs4 import BeautifulSoup
import requests
import sys, urllib.parse, pyperclip

search_item = sys.argv[1:]
if not search_item:
    search_item = pyperclip.paste()

# I used headers because pypi was blocking my request 
headers = {
    "User-Agent": "Mozilla/5.0" 

}
encoded_search = urllib.parse.quote(search_item)
url = f"https://pypi.org/search/?q={encoded_search}"
response = requests.get(url, headers= headers)
html = response.text
soup = BeautifulSoup(html,'lxml')
#print(soup.prettify())
print(response.status_code)

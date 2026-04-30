import requests
from bs4 import BeautifulSoup

def get_xkdc(url, num_downloads):
    if num_downloads < 5:
        response = requests.get(url)

        if response.status_code != requests.codes.ok:
            print("Error occured: " ,response.status_code)
            return 

        html = response.text
        soup = BeautifulSoup(html, "lxml")

        comics = soup.select_one("#comic img") #This helps us find img inside div id = "comic" and returns the first one
        comic_url = "https:"+comics["src"]
        print(comic_url)
        prev = soup.select_one('a[rel = "prev"]')
        prev_url = "https://xkcd.com"+prev["href"]

        # Use stream=True to handle large files efficiently
        res = requests.get(comic_url, stream= True)
        if res.ok:
            with open(f"C:\\python projects\\Web_scraping\\comic_img{num_downloads}.jpg","wb") as f:
                # Write the file in 1KB chunks
                for chunk in res.iter_content(1024):
                    f.write(chunk)
            print("Download successful!")
        else:
            print(f"Failed: Status code {res.status_code}")

        get_xkdc(prev_url, num_downloads + 1)
    
    else:
        print("DONE!!!")

    
    #print(soup.prettify())

get_xkdc("https://xkcd.com/",1)
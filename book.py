import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pathlib import Path
base_url = "https://books.toscrape.com/"

def get_book_info(book_url,genre,con):
    page = requests.get(book_url)
    soup2 = BeautifulSoup(page.content,'lxml')
    book_card = soup2.find_all("article")
    #[Title, Price, Availability,Rating,Link]
    mode = "w" if con == 1 else "a"
    file_path = Path(__file__).parent/f"{genre}.csv"
    with open(file_path,mode, encoding = "utf-8", newline= "") as csv_file:
        writer = csv.writer(csv_file)
        if con == 1:
            writer.writerow(["Name","Price","Availability","Rating","Link"])#Column names
        for b in book_card:
            book_info = b.find("h3").a
            link = book_info["href"]
            name = book_info["title"]
            product_price = b.find("p",class_="price_color")
            price = product_price.text
            is_available = b.find("p", class_= "instock availability")       
            availability = is_available.text
            book_rating = b.find("p", class_= "star-rating")
            rating = book_rating["class"][1]    
            writer.writerow([name, price, availability, rating, link])

        if con < 4:
                second = soup2.find("ul",class_ = "pager")
                if second:
                    next_link = second.find("a")["href"]
                    next_url = urljoin(book_url,next_link)
                    get_book_info(next_url,genre,con + 1)
    
        print(f"Writing to file {genre}")


url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
Category = ["Thriller", "Fiction", "Religion","Fantasy","Poetry"]

result = soup.find("div", class_="side_categories")
genre = result.find_all("a",string = lambda text: text and text.strip() in Category)
#print(genre)
for r in genre:
    genre_link = r["href"]
    full_url = urljoin(base_url,genre_link)
    genre_name = r.text.strip()
    get_book_info(full_url,genre_name,1)
    #print(full_url)
    #https://books.toscrape.com/catalogue/category/books/fiction_10/index.html
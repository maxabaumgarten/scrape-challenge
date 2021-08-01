  
###########################################################
############## Created by Max Baumgarten ##################
###########################################################

# import required libraries

import csv
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

# create csv file to store data
filename = 'data.csv'
f = open(filename, 'w')

# science catergory url
science_url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
base_url = "http://books.toscrape.com/catalogue/"

# get each book url from science_url
response = requests.get(science_url)
soup = BeautifulSoup(response.text, "html.parser")
book_urls = soup.find_all("article", class_="product_pod")
book_urls = [book.find("a")["href"] for book in book_urls]

# loop through each book url
for book_url in book_urls:

    # get name, price, Product Description, UPC, Product Type, Tax, Number of reviews of book and store in csv file
    joined_url = urljoin(base_url, book_url)
    print(joined_url)
    response = requests.get(joined_url)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find("h1", class_="product_name").text.strip()
    price = soup.find("p", class_="price_color").text.strip()
    product_description = soup.find("div", class_="product_description").text.strip()
    upc = soup.find("span", class_="upc").text.strip()
    product_type = soup.find("p", class_="product_type").text.strip()
    tax = soup.find("p", class_="tax").text.strip()
    number_of_reviews = soup.find("p", class_="star-rating").text.strip()
    f.write(name + "," + price + "," + product_description + "," + upc + "," + product_type + "," + tax + "," + number_of_reviews + "\n")

# poetry catergory url
poetry_url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"

# get each book url from science_url
response = requests.get(poetry_url)
soup = BeautifulSoup(response.text, "html.parser")
book_urls = soup.find_all("article", class_="product_pod")
book_urls = [book.find("a")["href"] for book in book_urls]

# loop through each book url
for book_url in book_urls:

    # get name, price, Product Description, UPC, Product Type, Tax, Number of reviews of book and store in csv file
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, "html.parser")
    name = soup.find("h1", class_="product_name").text.strip()
    price = soup.find("p", class_="price_color").text.strip()
    product_description = soup.find("div", class_="product_description").text.strip()
    upc = soup.find("span", class_="upc").text.strip()
    product_type = soup.find("p", class_="product_type").text.strip()
    tax = soup.find("p", class_="tax").text.strip()
    number_of_reviews = soup.find("p", class_="star-rating").text.strip()
    f.write(name + "," + price + "," + product_description + "," + upc + "," + product_type + "," + tax + "," + number_of_reviews + "\n")

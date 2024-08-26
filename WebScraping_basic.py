import requests
from bs4 import BeautifulSoup

# Get the url of a test site
url="https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

# To check whether we can extract the html data of a particular site
r=requests.get(url)
print(r)

# To print entire html
soup=BeautifulSoup(r.text, "lxml")
print(soup)

# To retrieve each box on the page
boxes=soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
print(len(boxes))

# To retrieve names of each product on the page
product_name=soup.find_all("a",class_="title")
print(product_name)

# To print only the name(above print the name along with the html)
for i in product_name:
    print(i.text)

# To retrieve price of each product on the page
product_price=soup.find_all("h4",class_="price float-end card-title pull-right")
print(product_price)

# To print only the price(above print the price along with the html)
for i in product_price:
    print(i.text)
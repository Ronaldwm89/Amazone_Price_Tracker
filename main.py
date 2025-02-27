import requests
from bs4 import BeautifulSoup 

url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)
website_soup = BeautifulSoup(response.text, "html.parser")

precio = website_soup.find('span', class_='a-price-whole').getText()
centimos = website_soup.find('span', class_='a-price-fraction').getText()

precio_total = float(precio) + float(centimos) / 100



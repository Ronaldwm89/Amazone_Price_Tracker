import requests
import smtplib 
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

print(f"Email: {EMAIL}")

def get_price():
    url = "https://appbrewery.github.io/instant_pot/"
    response = requests.get(url)
    website_soup = BeautifulSoup(response.text, "html.parser")

    precio = website_soup.find('span', class_='a-price-whole').getText()
    centimos = website_soup.find('span', class_='a-price-fraction').getText()

    precio_total = float(precio) + float(centimos) / 100
    
    return precio_total

def send_email():
    COST = get_price()
    #MY_EMAIL = 
    #MY_PASSWORD = 

    #if COST < 100:
        #with smtplib**


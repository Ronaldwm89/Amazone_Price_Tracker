import requests
import smtplib 
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email.message import EmailMessage
import os

load_dotenv() # Load environment variables

# Headers to avoid being blocked
headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}


# Constants data from .env file
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
URL = "https://appbrewery.github.io/instant_pot/"

# Function to get the price of the product
def get_price():
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    website_soup = BeautifulSoup(response.text, "html.parser")

    precio = website_soup.find('span', class_='a-price-whole').getText()
    centimos = website_soup.find('span', class_='a-price-fraction').getText()

    precio_total = float(precio) + float(centimos) / 100
    
    return precio_total

#Create the email message
def create_email():
    msg = EmailMessage()
    msg['Subject'] = '!!ALERT!! It´s time to buy'
    msg['From'] = EMAIL
    msg['To'] = 'ronmed1989@yahoo.com'
    msg.set_content(f'Time to buy, the product is under 100$ you should buy it now\n {URL}')
    return msg

#Function to send the email
def send_email():
    COST = get_price()
    MSG = create_email()
    
    if COST < 100:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(MSG)

send_email()


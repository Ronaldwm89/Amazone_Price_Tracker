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

#Constants
URL = "https://www.amazon.com/-/es/Xbox-X/dp/B08H75RTZ8/ref=sr_1_3?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=YG71JE1MVQ1K&dib=eyJ2IjoiMSJ9.DQ7dQ2Wdt7c6lzUHbPD5EWMCM-xDz5N25sJju9s9P8zwv8yQw8phqZ0i684CK9SscmGakqvCpyolR_QswAlipHPIYbI_QUbh5-ielKpV2W3AHp-BaQM2vQHF8QztIABjRMBmQUwR3U-2l4wQL9la-rMNQ4mI19Xr-hB2-th015Mi-odXmLk7zR0qFl5k9bNU67G_q_nvx27LeYuHxqi0SjsIa8oGjlUduKTspWuH4JM.vr4c4louB0zQH_miLsMYoE6qtJof0bieBxdmK5sO-aE&dib_tag=se&keywords=xbox&qid=1740784139&sprefix=xbo%2Caps%2C217&sr=8-3&th=1"
PRICE_STIMATE = 500

# Function to get the price of the product
def get_price():
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    website_soup = BeautifulSoup(response.text, "html.parser")

    title = website_soup.find('span', id='productTitle').getText(strip=True)
    precio = website_soup.find('span', class_='a-price-whole').getText()
    centimos = website_soup.find('span', class_='a-price-fraction').getText()

    precio_total = float(precio) + float(centimos) / 100
    

    print(website_soup.prettify())
    #return precio_total, title
get_price()
#Create the email message
def create_email():
    PRODUCT = get_price()[1]
    msg = EmailMessage()
    msg['Subject'] = '!!ALERT!! It´s time to buy'
    msg['From'] = EMAIL
    msg['To'] = 'ronmed1989@yahoo.com'
    msg.set_content(f'Time to buy, the {PRODUCT} is under {PRICE_STIMATE} you should buy it now\n {URL}')
    return msg

#Function to send the email
def send_email():
    COST = get_price()[0]
    MSG = create_email()
    
    if COST < PRICE_STIMATE:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(MSG)

#send_email()
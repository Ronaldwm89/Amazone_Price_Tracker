import requests
import smtplib 
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email.message import EmailMessage
import os

load_dotenv() # Load environment variables

# Constants data from .env file
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Function to get the price of the product
def get_price():
    url = "https://appbrewery.github.io/instant_pot/"
    response = requests.get(url)
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
    msg.set_content('Time to buy, the product is under 100 you should buy it now')
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



from ast import While
import requests
import csv
from bs4 import BeautifulSoup
import time
import smtplib
from email.message import EmailMessage
import smtplib, ssl

#in page you should find the price of the product (html)
page = requests.get('https://www.allkeyshop.com/blog/catalogue/category-nintendo-switch/search-binding/', verify=False)
soup = BeautifulSoup(page.text, 'html.parser')

# Pull all text from the BodyText div
precio2 = soup.find(class_='search-results-row-price')
print(precio2)
precio=precio2
precio = precio.text.replace("€","").strip()
precio = float(precio)



def checkprice():
    oferta=False
    while True:
        if (precio>=39.99):
            pass
        else:
            oferta=True
        while(oferta==True):
            email_alert()
            break

        time.sleep(7200)



def email_alert():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "x@gmail.com" 
    receiver_email = "x@gmail.com" #same email   
    password = "x"
    message = """"Price is lower than expected"""""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

checkprice()

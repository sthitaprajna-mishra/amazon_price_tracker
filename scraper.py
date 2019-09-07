import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Blue-Balance-Bike-Special-Needs/dp/B07SLNK3QN/ref=sr_1_7?keywords=bike&qid=1567857472&s=specialty-aps&sr=1-7'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

def check_price():
	page = requests.get(URL, headers = headers)

	soup1 = BeautifulSoup(page.content, "html.parser")

	soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

	title = soup2.find(id= "productTitle").text.strip()
	price = soup2.find(id = "priceblock_ourprice").text
	converted_price = float(price[1:3])

	print(title)
	print("\n")
	print(converted_price)

	if (converted_price > 80.00):
		send_mail()

def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('sthitaprajna360@gmail.com', 'gjlcopycohlszqxy')
	subject = 'Price fell down!'
	body = 'Check the Amazon link https://www.amazon.com/Blue-Balance-Bike-Special-Needs/dp/B07SLNK3QN/ref=sr_1_7?keywords=bike&qid=1567857472&s=specialty-aps&sr=1-7'
	msg = f"Subject: {subject} \n\n {body}"
	server.sendmail('sthitaprajna360@gmail.com', 'sthitaprajna360@gmail.com', msg)
	print("Email has been sent!")
	server.quit()

check_price()
'''
while (True):
	check_price()
	time.sleep(60*60*24)
'''
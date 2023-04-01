'''
This script scraps data from the stores url and it checks for current price and if current price
is less than the threshold set by user, it will also send mail to mail_id set up by user

Author : VIVEKSUREKA (Vivek Sureka)
'''

from bs4 import BeautifulSoup
import requests
import smtplib
import datetime
import os
import csv
import time

with open('config.txt','r') as file:
        reader = csv.reader(file,delimiter = '\n')
        cnt = 0
        for row in reader:
            if(cnt==0):
                your_header=row[0]
                cnt = cnt+1
            elif(cnt==1):
                url = row[0]
                cnt= cnt+1
            elif(cnt==2):
                prod_class_name = row[0]
                cnt=cnt+1
            elif(cnt==3):
                price_class_name = row[0]
                cnt = cnt+1 
            elif(cnt==4):
                mail_id = row[0]
                cnt = cnt+1
            elif(cnt==5):
                passcode = row[0]
                cnt = cnt+1
            elif(cnt==6):
                threshold = float(row[0])
                cnt = cnt+1        
            
        

def check_price():
    headers = {'User-Agent' : your_header}

    webpage = requests.get(url, headers = headers)

    bs = BeautifulSoup(webpage.content,'html.parser')
    
    prod_name = bs.find('span',{"class":prod_class_name}).get_text()
    price = (float)(bs.find("div",{"class":price_class_name}).get_text()[1:].replace(',',''))

    print(prod_name)
    return price,prod_name


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    print("logging in....")
    server.login(mail_id, passcode)
    subj = "HEY! PRICE OF YOUR FAVOURITE PRODUCT FELL DOWN"
    body = f"Your favourite product is at it's best price! Click on the below link to order now\n Link=> {url} \n Regards\n Get Best Price"
    message = f"subject: {subj}\n\n\n{body}"
    print("sending mail....")
    server.sendmail(mail_id,mail_id,message)
    print("Email sent successfully\n logging out....")
    server.quit()
    print("successfully logged out of mail!")


def store_price():
    path = "./"+prod_name.replace(' ','_')+".csv"
    if not os.path.exists(path):
        with open(path,'w') as file:
            writer = csv.writer(file,lineterminator ="\n")
            headings = ["Timestamps", "price(INR)"]
            writer.writerow(headings)

    with open(path,'a') as file:
        writer = csv.writer(file,lineterminator ="\n")
        timestamp = f"{datetime.datetime.date(datetime.datetime.now())} , {datetime.datetime.time(datetime.datetime.now())}"
        writer.writerow([timestamp,price])
        print("Added entry to csv file")

while True:
    price,prod_name = check_price()
    store_price()
    if(price<threshold):
        sendMail()
        threshold = price
    time.sleep(2*60*60)

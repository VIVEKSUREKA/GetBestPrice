'''
This is main program which will take necessary information for keeping track of prices of your
favourite product and calls scraper.py and plotter.py as per the requirement.

Author : VIVEKSUREKA (Vivek Sureka)
'''

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget,QFileDialog, QGridLayout, QLineEdit, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import os
from bs4 import BeautifulSoup
import requests
import csv
import time
import subprocess


widgets = {
    "logo":[],
    "button":[],
    "labels":[],
    "text_box":[]
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Get Best Price")
window.setFixedWidth(1000)
window.move(400,200)
#window.setWindowState(QtCore.Qt.WindowMaximized)
window.setStyleSheet("background:#2534c9;")

grid = QGridLayout()

# br_header=""
# prod_url=""
# name_class=""
# price_class=""
# email=""
# pas=""

def clear_window():
    for widget in widgets:
        if widgets[widget]!=[]:
            widgets[widget][-1].hide()
        for i in range(0,len(widgets[widget])):
            widgets[widget].pop()


detail = {"header":"","url":"","prod_class":"","price_class":"","mail_id":"","passcode":""}

def report_price():    
    if os.path.exists("./config.txt"):
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
        headers = {'User-Agent' : your_header}

        webpage = requests.get(url, headers = headers)

        bs = BeautifulSoup(webpage.content,'html.parser')
        prod_name = bs.find('span',{"class":prod_class_name}).get_text()
        price = (float)(bs.find("div",{"class":price_class_name}).get_text()[1:].replace(',',''))
        print(prod_name)
        return price,prod_name

def price_plot():
    os.system("python plotter.py")

def home():
    if os.path.exists("./config.txt"):
        price,prod = report_price()
        window.setStyleSheet("background:'white';")
        #heading
        heading = QLabel("Get Best Price! Don't pay more!")
        heading.setStyleSheet(
            "background:#ed6c21;"+
            "color:'white';"+
            "font-size:36px;"+
            "padding: 0 0 25px 10px;"+
            "font-weight:bold;"
        )
        heading.setFixedHeight(75)
        heading.setAlignment(QtCore.Qt.AlignCenter)
        widgets["labels"].append(heading)

        info = QLabel("You are all set! you will receive mail when price of your favourite product goes below threshold value")
        info.setStyleSheet(
            "color:'black';"+
            "font-size:20px;"+
            "padding: 0 0 25px 10px;"+
            "font-weight:bold;"
        )
        info.setAlignment(QtCore.Qt.AlignCenter)
        
        product = QLabel("Product name : "+str(prod))
        product.setStyleSheet(
            "color:'black';"+
            "font-size:20px;"+
            "padding: 0 0 25px 10px;"+
            "font-weight:bold;"
        )
        product.setAlignment(QtCore.Qt.AlignCenter)
        price_of_prod = QLabel("Current price of product : "+str(price))
        price_of_prod.setStyleSheet(
            "color:'black';"+
            "font-size:20px;"+
            "padding: 0 0 25px 10px;"+
            "font-weight:bold;"
        )
        price_of_prod.setAlignment(QtCore.Qt.AlignCenter)

        #plot_button
        submit_button = QPushButton("Monitor price?")
        submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        submit_button.setStyleSheet(
            "*{border:1px solid 'black';"+
            "border-radius: 20px;"+
            "font-size: 20px;"+
            "margin:100px 400px;"+
            "color:'black';}"
            "*:hover{background: 'blue';"+
            "color:'white';}"
        )
        widgets["button"].append(submit_button)
        submit_button.clicked.connect(lambda:price_plot())

        #credits
        cred = QLabel("Made with <3 by Vivek")
        cred.setStyleSheet(
            "background:'black';"+
            "color:'white';"+
            "font-weight:bold;"
        )
        cred.setAlignment(QtCore.Qt.AlignCenter)
        cred.setFixedHeight(25)
        widgets["labels"].append(cred)

        grid.addWidget(heading,0,0,1,2)
        grid.addWidget(info,1,0,1,2)
        grid.addWidget(product,2,0,1,2)
        grid.addWidget(price_of_prod,3,0,1,2)
        grid.addWidget(submit_button,5,0,2,2)
        grid.addWidget(cred,7,0,1,2)
        
        # while True:
        #     os.system("python scraper.py")
        #     time.sleep(60*60)

        # os.system("python scraper.py")
        # time.sleep(60*60)


def set_threshold(threshold_price):
    if os.path.exists("./config.txt"):
        with open("./config.txt",'a') as file:
            file.write(threshold_price)
            file.write("\n")
        clear_window()
        home()

def lastframe():
    if os.path.exists("./config.txt"):
        price,prod = report_price()
        window.setStyleSheet("background:'white';")
        #heading
        heading = QLabel("Get Best Price! Don't pay more!")
        heading.setStyleSheet(
            "background:#ed6c21;"+
            "color:'white';"+
            "font-size:36px;"+
            "padding: 0 0 25px 10px;"+
            "font-weight:bold;"
        )
        heading.setFixedHeight(75)
        heading.setAlignment(QtCore.Qt.AlignCenter)
        widgets["labels"].append(heading)

        product = QLabel("Product name : "+str(prod))
        product.setStyleSheet(
            "color:'black';"+
            "font-size:20px;"+
            "padding: 0 0 25px 10px;"+
            "font-weight:bold;"
        )
        product.setAlignment(QtCore.Qt.AlignCenter)
        price_of_prod = QLabel("Current price of product : "+str(price))
        price_of_prod.setStyleSheet(
            "color:'black';"+
            "font-size:20px;"+
            "padding: 0 0 25px 10px;"+
            "font-weight:bold;"
        )
        price_of_prod.setAlignment(QtCore.Qt.AlignCenter)
        thres = QLabel("Set the threshold value of price : ")
        thres.setStyleSheet(
            "color:'black';"+
            "font-size:20px;"+
            "padding: 0 0 25px 10px;"+
            "font-weight:bold;"
        )
        thres.setAlignment(QtCore.Qt.AlignCenter)
        threshold = QLineEdit()
        threshold.setStyleSheet(
            "QLineEdit"
            "{background:'white';"+
            "margin:10px 400px;}"
        )
        threshold.setAlignment(QtCore.Qt.AlignCenter)
        widgets["text_box"].append(threshold)

        #submit_button
        submit_button = QPushButton("Set Threshold")
        submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        submit_button.setStyleSheet(
            "*{border:1px solid 'black';"+
            "border-radius: 20px;"+
            "font-size: 20px;"+
            "margin:100px 400px;"+
            "color:'black';}"
            "*:hover{background: 'blue';"+
            "color:'white';}"
        )
        # submit_button.setFixedHeight(200)
        # submit_button.setFixedWidth(300)
        widgets["button"].append(submit_button)
        # s = "passcode"
        submit_button.clicked.connect(lambda:set_threshold(threshold.text()))
        
        #credits
        cred = QLabel("Made with <3 by Vivek")
        cred.setStyleSheet(
            "background:'black';"+
            "color:'white';"+
            "font-weight:bold;"
        )
        cred.setAlignment(QtCore.Qt.AlignCenter)
        cred.setFixedHeight(25)
        widgets["labels"].append(cred)

        grid.addWidget(heading,0,0,1,2)
        grid.addWidget(product,1,0)
        # grid.addWidget(product_name,1,1)
        grid.addWidget(price_of_prod,2,0)
        # grid.addWidget(price_val,2,1)
        grid.addWidget(thres,3,0)
        grid.addWidget(threshold,4,0)
        grid.addWidget(submit_button,5,0,3,1)
        grid.addWidget(cred,7,0,1,2)

def write_to_config():
    with open("./config.txt",'w') as file:
        file.write(detail["header"])
        file.write("\n")
        file.write(detail["url"])
        file.write("\n")
        file.write(detail["prod_class"])
        file.write("\n")
        file.write(detail["price_class"])
        file.write("\n")
        file.write(detail["mail_id"])
        file.write("\n")
        file.write(detail["passcode"])
        file.write("\n")
    clear_window()
    lastframe()

def details_passcode(value,key):
    detail[key]=value
    clear_window()
    write_to_config()

def fill_passcode():
    window.setStyleSheet("background:'white';")
    #heading
    heading = QLabel("Fill necessary details...")
    heading.setStyleSheet(
        "background:#ed6c21;"+
        "color:'white';"+
        "font-size:36px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    heading.setFixedHeight(75)
    heading.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(heading)

    #passcode_instruction
    passcode_box = QLabel("Type your app passcode generated from gmail using 2 layer authentication\nWe don't collect or store any credentials!")
    passcode_box.setStyleSheet(
        "color:'orange';"+
        "font-size:20px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    passcode_box.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(passcode_box)

    #passcode_text
    passcode_text = QLineEdit()
    passcode_text.setStyleSheet(
        "QLineEdit"
        "{background:'white';"+
        "margin:10px 100px;}"
    )
    passcode_text.setAlignment(QtCore.Qt.AlignCenter)
    widgets["text_box"].append(passcode_text)

    #submit_button
    submit_button = QPushButton("Submit")
    submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    submit_button.setStyleSheet(
        "*{border:1px solid 'black';"+
        "border-radius: 20px;"+
        "font-size: 20px;"+
        "margin:100px 400px;"+
        "color:'black';}"
        "*:hover{background: 'blue';"+
        "color:'white';}"
    )
    # submit_button.setFixedHeight(200)
    # submit_button.setFixedWidth(300)
    widgets["button"].append(submit_button)
    s = "passcode"
    submit_button.clicked.connect(lambda:details_passcode(passcode_text.text(),s))
    

    #credits
    cred = QLabel("Made with <3 by Vivek")
    cred.setStyleSheet(
        "background:'black';"+
        "color:'white';"+
        "font-weight:bold;"
    )
    cred.setAlignment(QtCore.Qt.AlignCenter)
    cred.setFixedHeight(25)
    widgets["labels"].append(cred)

    grid.addWidget(heading,0,0)
    grid.addWidget(passcode_box,1,0)
    grid.addWidget(passcode_text,2,0)
    grid.addWidget(submit_button,3,0,3,1)
    grid.addWidget(cred,5,0,1,2)

def details_mail_id(value,key):
    detail[key]=value
    clear_window()
    fill_passcode()

def fill_mail_id():
    window.setStyleSheet("background:'white';")
    #heading
    heading = QLabel("Fill necessary details...")
    heading.setStyleSheet(
        "background:#ed6c21;"+
        "color:'white';"+
        "font-size:36px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    heading.setFixedHeight(75)
    heading.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(heading)

    #mail_id_instruction
    mail_id_box = QLabel("Type your email id on which you would like to get best deals")
    mail_id_box.setStyleSheet(
        "color:'dark blue';"+
        "font-size:24px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    mail_id_box.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(mail_id_box)

    #mail_id_text
    mail_id_text = QLineEdit()
    mail_id_text.setStyleSheet(
        "QLineEdit"
        "{background:'white';"+
        "margin:10px 100px;}"
    )
    mail_id_text.setAlignment(QtCore.Qt.AlignCenter)
    widgets["text_box"].append(mail_id_text)

    #submit_button
    submit_button = QPushButton("Submit")
    submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    submit_button.setStyleSheet(
        "*{border:1px solid 'black';"+
        "border-radius: 20px;"+
        "font-size: 20px;"+
        "margin:100px 400px;"+
        "color:'black';}"
        "*:hover{background: 'blue';"+
        "color:'white';}"
    )
    # submit_button.setFixedHeight(200)
    # submit_button.setFixedWidth(300)
    widgets["button"].append(submit_button)
    s = "mail_id"
    submit_button.clicked.connect(lambda:details_mail_id(mail_id_text.text(),s))    

    #credits
    cred = QLabel("Made with <3 by Vivek")
    cred.setStyleSheet(
        "background:'black';"+
        "color:'white';"+
        "font-weight:bold;"
    )
    cred.setAlignment(QtCore.Qt.AlignCenter)
    cred.setFixedHeight(25)
    widgets["labels"].append(cred)

    grid.addWidget(heading,0,0)
    # grid.addWidget(logo,0,1)
    grid.addWidget(mail_id_box,1,0)
    grid.addWidget(mail_id_text,2,0)
    grid.addWidget(submit_button,3,0,3,1)
    grid.addWidget(cred,5,0,1,2)

def details_price(value,key):
    detail[key] = value
    clear_window()
    fill_mail_id()

def fill_price_class_box():
    window.setStyleSheet("background:'white';")
    #heading
    heading = QLabel("Fill necessary details...")
    heading.setStyleSheet(
        "background:#ed6c21;"+
        "color:'white';"+
        "font-size:36px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    heading.setFixedHeight(75)
    heading.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(heading)

    

    #paste_price_class_textbox_instruction
    price_class_box = QLabel("Inspect element and paste the name of class associated with price (generally it is '_30jeq3 _16Jk6d'): ")
    price_class_box.setStyleSheet(
        "color:'purple';"+
        "font-size:24px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    price_class_box.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(price_class_box)

    #price_class_text
    price_class_text = QLineEdit()
    price_class_text.setStyleSheet(
        "QLineEdit"
        "{background:'white';"+
        "margin:10px 100px;}"
    )
    price_class_text.setAlignment(QtCore.Qt.AlignCenter)
    widgets["text_box"].append(price_class_text)

    
    #submit_button
    submit_button = QPushButton("Submit")
    submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    submit_button.setStyleSheet(
        "*{border:1px solid 'black';"+
        "border-radius: 20px;"+
        "font-size: 20px;"+
        "margin:100px 400px;"+
        "color:'black';}"
        "*:hover{background: 'blue';"+
        "color:'white';}"
    )
    # submit_button.setFixedHeight(200)
    # submit_button.setFixedWidth(300)
    widgets["button"].append(submit_button)
    s = "price_class"
    submit_button.clicked.connect(lambda:details_price(price_class_text.text(),s))
    
    #credits
    cred = QLabel("Made with <3 by Vivek")
    cred.setStyleSheet(
        "background:'black';"+
        "color:'white';"+
        "font-weight:bold;"
    )
    cred.setAlignment(QtCore.Qt.AlignCenter)
    cred.setFixedHeight(25)
    widgets["labels"].append(cred)

    grid.addWidget(heading,0,0)
    # grid.addWidget(logo,0,1)
    grid.addWidget(price_class_box,1,0)
    grid.addWidget(price_class_text,2,0)
    grid.addWidget(submit_button,3,0,3,1)
    grid.addWidget(cred,5,0,1,2)

def details_prod(value,key):
    detail[key]=value
    clear_window()
    fill_price_class_box()

def fill_prod_class():
    window.setStyleSheet("background:'white';")
    #heading
    heading = QLabel("Fill necessary details...")
    heading.setStyleSheet(
        "background:#ed6c21;"+
        "color:'white';"+
        "font-size:36px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    heading.setFixedHeight(75)
    heading.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(heading)

    #paste_prod_class_textbox_instruction
    prod_class_box = QLabel("Inspect element and paste the name of class associated with product name (generally it is 'B_NuCI'):")
    prod_class_box.setStyleSheet(
        "color:'red';"+
        "font-size:24px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    prod_class_box.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(prod_class_box)

    #prod_class_text
    prod_class_text = QLineEdit()
    prod_class_text.setStyleSheet(
            "QLineEdit"
        "{background:'white';"+
        "margin:10px 100px;}"
    )
    prod_class_text.setAlignment(QtCore.Qt.AlignCenter)
    widgets["text_box"].append(prod_class_text)
    
    #submit_button
    submit_button = QPushButton("Submit")
    submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    submit_button.setStyleSheet(
        "*{border:1px solid 'black';"+
        "border-radius: 20px;"+
        "font-size: 20px;"+
        "margin:100px 400px;"+
        "color:'black';}"
        "*:hover{background: 'blue';"+
        "color:'white';}"
    )
    # submit_button.setFixedHeight(200)
    # submit_button.setFixedWidth(300)
    widgets["button"].append(submit_button)
    s = "prod_class"
    submit_button.clicked.connect(lambda:details_prod(prod_class_text.text(),s))


    #credits
    cred = QLabel("Made with <3 by Vivek")
    cred.setStyleSheet(
        "background:'black';"+
        "color:'white';"+
        "font-weight:bold;"
    )
    cred.setAlignment(QtCore.Qt.AlignCenter)
    cred.setFixedHeight(25)
    widgets["labels"].append(cred)

    grid.addWidget(heading,0,0)
    # grid.addWidget(logo,0,1)
    grid.addWidget(prod_class_box,1,0)
    grid.addWidget(prod_class_text,2,0)
    grid.addWidget(submit_button,3,0,3,1)
    grid.addWidget(cred,5,0,1,2)

def details_url(value,key):
    detail[key]=value
    clear_window()
    fill_prod_class()

def fill_url():
    window.setStyleSheet("background:'white';")
    #heading
    heading = QLabel("Fill necessary details...")
    heading.setStyleSheet(
        "background:#ed6c21;"+
        "color:'white';"+
        "font-size:36px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    heading.setFixedHeight(75)
    heading.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(heading)


    #paste_url_textbox_instruction
    url = QLabel("Paste the url of your favourite product's fl*pk*rt page")
    url.setStyleSheet(
        "color:'blue';"+
        "font-size:24px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    url.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(url)

    #url_text
    url_text = QLineEdit()
    url_text.setStyleSheet(
        "QLineEdit"
        "{background:'white';"+
        "margin:10px 100px;}"
    )
    url_text.setAlignment(QtCore.Qt.AlignCenter)
    widgets["text_box"].append(url_text)
    
    #submit_button
    submit_button = QPushButton("Submit")
    submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    submit_button.setStyleSheet(
        "*{border:1px solid 'black';"+
        "border-radius: 20px;"+
        "font-size: 20px;"+
        "margin:100px 400px;"+
        "color:'black';}"
        "*:hover{background: 'blue';"+
        "color:'white';}"
    )
    # submit_button.setFixedHeight(200)
    # submit_button.setFixedWidth(300)
    widgets["button"].append(submit_button)
    s = "url"
    submit_button.clicked.connect(lambda:details_url(url_text.text(),s))
    

    #credits
    cred = QLabel("Made with <3 by Vivek")
    cred.setStyleSheet(
        "background:'black';"+
        "color:'white';"+
        "font-weight:bold;"
    )
    cred.setAlignment(QtCore.Qt.AlignCenter)
    cred.setFixedHeight(25)
    widgets["labels"].append(cred)

    grid.addWidget(heading,0,0)
    # grid.addWidget(logo,0,1)
    grid.addWidget(url,1,0)
    grid.addWidget(url_text,2,0)
    grid.addWidget(submit_button,3,0,3,1)
    grid.addWidget(cred,5,0,1,2)

def details_header(value,key):
    detail[key]=value
    clear_window()
    fill_url()

def fill_header():
    window.setStyleSheet("background:'white';")
    #heading
    heading = QLabel("Fill necessary details...")
    heading.setStyleSheet(
        "background:#ed6c21;"+
        "color:'white';"+
        "font-size:36px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    heading.setFixedHeight(75)
    heading.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(heading)

    #paste_header_textbox_instruction
    header_box = QLabel("Paste the user-agent for your system(Search 'what is my user-agent?' on google)")
    header_box.setStyleSheet(
        "color:'green';"+
        "font-size:24px;"+
        # "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    header_box.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(header_box)

    #header_text
    header_text = QLineEdit()
    header_text.setStyleSheet(
        "QLineEdit"
        "{background:'white';"+
        "margin:10px 100px;}"
    )
    header_text.setAlignment(QtCore.Qt.AlignCenter)
    widgets["text_box"].append(header_text)
    
    #submit_button
    submit_button = QPushButton("Submit")
    submit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    submit_button.setStyleSheet(
        "*{border:1px solid 'black';"+
        "border-radius: 20px;"+
        "font-size: 20px;"+
        "margin:100px 400px;"+
        "color:'black';}"
        "*:hover{background: 'blue';"+
        "color:'white';}"
    )
    # submit_button.setFixedHeight(200)
    # submit_button.setFixedWidth(300)
    widgets["button"].append(submit_button)
    s = "header"
    submit_button.clicked.connect(lambda:details_header(header_text.text(),s))
    

    #credits
    cred = QLabel("Made with <3 by Vivek")
    cred.setStyleSheet(
        "background:'black';"+
        "color:'white';"+
        "font-weight:bold;"
    )
    cred.setAlignment(QtCore.Qt.AlignCenter)
    cred.setFixedHeight(25)
    widgets["labels"].append(cred)

    grid.addWidget(heading,0,0,1,2)
    # grid.addWidget(logo,0,1)
    grid.addWidget(header_box,1,0)
    grid.addWidget(header_text,2,0)
    grid.addWidget(submit_button,3,0,3,1)
    grid.addWidget(cred,5,0,1,2)

def details_required():
    clear_window()
    fill_header()

def getStarted():
    '''
    This screen appears only first time in order to set up config.txt
    '''
    #logo
    image = QPixmap("logo1.png")
    logo1 = QLabel()
    logo1.setPixmap(image)
    logo1.setAlignment(QtCore.Qt.AlignCenter)
    logo1.setStyleSheet("margin-top: 50px")
    widgets["logo"].append(logo1)

    #text
    intro1 = QLabel("Welcome to Get Best Price!")
    intro1.setStyleSheet(
        "color:'#ed6c21';"+
        "font-size:36px;"+
        "padding: 0 0 25px 10px;"+
        "font-weight:bold;"
    )
    intro1.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(intro1)

    #text
    intro2 = QLabel("Select your favourite item and purchase it at best price!")
    intro2.setStyleSheet(
        "color:'white';"+
        "font-size:28px;"+
        "font-family: 'Times New Roman';"+
        "font-style:italic;"
    )
    intro2.setAlignment(QtCore.Qt.AlignCenter)
    widgets["labels"].append(intro2)

    #Config-button
    button = QPushButton("Get Started!")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border:4px solid '#ed6c21';"+
        "border-radius: 45px;"+
        "font-size: 32px;"+
        "color:'white';"+
        "padding: 28px;"+
        "margin: 10px 150px 20px 150px;}"
        "*:hover{background: '#ed6c21'}"
    )
    widgets["button"].append(button)
    button.clicked.connect(details_required)


    grid.addWidget(logo1,0,0)
    grid.addWidget(intro1,1,0)
    grid.addWidget(intro2,2,0)
    grid.addWidget(button,3,0)


# def main():
    
if not os.path.exists("./config.txt"):
    getStarted()

p = subprocess.Popen([sys.executable, './scraper.py'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

home()

# getStarted()


window.setLayout(grid)
window.show()
app.exec()
p.kill()
sys.exit()

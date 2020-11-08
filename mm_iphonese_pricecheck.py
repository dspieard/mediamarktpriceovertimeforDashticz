import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

# Variables
url = "https://www.mediamarkt.nl/nl/product/_apple-iphone-se-128-gb-zwart-1659753.html"


# Grabbing the price from the IphoneSe
def grabprice():
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    price = soup.find_all("meta", {"itemprop" : "price"})

    # Slicing it to only show the price
    price = str(price)
    split_string = price.split('"', 1)
    sub_string = split_string[1]
    split_string = sub_string.split('"', 1)
    price = str(split_string[0])
    return price


# Grabbing the current date
def grabdate():
    dt = datetime.now()
    curdate = f"{dt.day}-{dt.month}-{dt.year}"
    return curdate


# Writing it to the csv file
def writetofile():
    with open ('iphonesemm.csv', 'a') as i:
        # Combining date and price
        fields = [grabdate(), grabprice()]
        writer = csv.writer(i)
        writer.writerow(fields)


writetofile()







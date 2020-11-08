import matplotlib.pyplot as plt
import csv
import requests
import base64
from io import BytesIO

from bs4 import BeautifulSoup
from datetime import datetime

# Checks the the price, creates a csv, makes a graph and creates a HTMLfile
class MMPriceChecker:
    def __init__(self, name, url, csvfilename, htmlfile):
        self.name = name
        self.url = url
        self.filename = csvfilename
        self.htmlfile = htmlfile

    tmpfile = BytesIO()

    # Grabbing the price
    def grabprice(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, 'html.parser')
        price = soup.find_all("meta", {"itemprop": "price"})

        # Slicing it to only show the price
        price = str(price)
        split_string = price.split('"', 1)
        sub_string = split_string[1]
        split_string = sub_string.split('"', 1)
        price = str(split_string[0])
        return price

    # Grabbing the current date
    def grabdate(self):
        dt = datetime.now()
        curdate = f"{dt.day}-{dt.month}-{dt.year}"
        return curdate

    # Writing it to the csv file
    def writetofile(self):
        with open(self.filename, 'a') as i:
            # Combining date and price
            fields = [self.grabdate(), self.grabprice()]
            writer = csv.writer(i)
            writer.writerow(fields)

    # Creating the graph
    def creategraph(self):
        with open(self.filename) as i:
            reader = csv.reader(i)

            dates, prices = [], []
            for row in reader:
                curdate = row[0]
                dates.append(curdate)

                price = int(row[1])
                prices.append(price)

        # Set chart title and label axes
        fig = plt.figure(dpi=65, figsize=(6, 6))
        plt.plot(dates, prices, c='blue')
        plt.title(f"{self.name} @ MediaMarkt", fontsize=16)
        plt.xlabel("Price", fontsize=12)
        plt.ylabel("Date", fontsize=12)
        plt.tick_params(axis='both', labelsize=10)
        # Save as html
        plt.savefig(self.tmpfile, format='png')

    # Create HTML
    def createhtml(self):
        encoded = base64.b64encode(self.tmpfile.getvalue()).decode('utf-8')
        html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
        with open(self.htmlfile, 'w') as f:
            f.write(html)

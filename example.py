from mmpricechecker import MMPriceChecker

# Variables (change this!)
url = "https://www.mediamarkt.nl/nl/product/_apple-iphone-se-128-gb-zwart-1659753.html" # link to MM product
filename = "iphonese.csv" # File where it stores the values (run the script every day to keep up-to-date info)
htmlname = "/home/pi/dev/dashticz/iphonese.html" # The html path + name which you can use in a Dashticz frame
name = "IphoneSE 128GB"


test = MMPriceChecker(name,url,filename,htmlname)
test.writetofile()
test.creategraph()
test.createhtml()

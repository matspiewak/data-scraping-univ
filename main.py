import requests
from bs4 import BeautifulSoup
import csv

rSklepklocki = requests.get("https://sklepklocki.pl/technic-c-74.html")
rSmyk = requests.get("https://www.smyk.com/lego-technic.html?limit=108&sortBy=price&sortOrder=asc")
rKrainazabawek = requests.get("https://www.krainazabawek24.pl/category/klocki-lego-technic/1/other/price/asc/0")

soupKz = BeautifulSoup(rKrainazabawek.text, 'html.parser')
soupSK = BeautifulSoup(rSklepklocki.text, 'html.parser')
soupS = BeautifulSoup(rSmyk.text, 'html.parser')

price_box_Krainazabawek = soupKz.find_all('span', attrs={'class': "price nowrap"})
name_box_Krainazabawek = soupKz.find_all('a', attrs={'class': "product_name"})

price_box_Sklepklocki = soupSK.find_all('span', attrs={'class': "Cena"})
name_box_Sklepklocki = soupSK.find_all('h3')

price_box_Smyk = soupS.find_all('span', attrs={'class': "price--new price--new--red"})
name_box_Smyk = soupS.find_all('div', attrs={'class': "complex-product__name"})

class products():
    def __init__(self, name, price):
        self.name = name
        self.price = price

kzList = []
sList = []
skList = []

for nameKZ,priceKZ,nameS,priceS,nameSK, priceSK in zip(
            name_box_Krainazabawek,price_box_Krainazabawek, name_box_Smyk,
            price_box_Smyk, name_box_Sklepklocki, price_box_Sklepklocki):
                sList.append(products(nameS.text.strip(),priceS.text.strip()))
                skList.append(products(nameSK.text.strip(), priceSK.text.strip()))
                kzList.append(products(nameKZ.text.strip(), priceKZ.text.strip()))

with open('scrappedData.csv', 'a') as file:
    writer = csv.writer(file)
    for o1,o2,o3 in zip(sList,skList,kzList):
        writer.writerow([o1.name,o1.price,o2.name,o2.price,o3.name,o3.price])

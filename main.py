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

kzList = []
sList = []
skList = []

for priceKZ, priceS, priceSK in zip(price_box_Krainazabawek, price_box_Smyk, price_box_Sklepklocki):
    sList.append(priceS.text.strip().replace('zł', '').replace(',', '.').replace(' ', ''))
    skList.append(priceSK.text.strip().replace('zł', '').replace(',', '.').replace(' ', ''))
    kzList.append(priceKZ.text.strip().replace('zł', '').replace(',', '.').replace(' ', ''))


def converter(products_list):
    for i in range(len(products_list)):
        products_list[i] = float(products_list[i])
    return products_list


avgKZ = converter(kzList)
avgS = converter(sList)
avgSK = converter(skList)


with open('scrappedData.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(["Kraina Zabawek", "Sklep-Klocki", "Smyk"])
    for o1, o2, o3 in zip(kzList, skList, sList):
        writer.writerow([o1, o2, o3])


def cal_avg(products_list):
    avg = sum(products_list)/len(products_list)
    return avg


avgKZ = cal_avg(kzList)
avgS = cal_avg(sList)
avgSK = cal_avg(skList)

with open('avgTechnicPrices.csv','a') as file:
    writer = csv.writer(file)
    writer.writerow(["Kraina Zabawek", "Sklep-Klocki", "Smyk"])
    writer.writerow([avgKZ, avgSK, avgS])


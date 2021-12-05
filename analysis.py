import requests 
from bs4 import BeautifulSoup as bs

link = "https://www.koronavakasayisi.com/"

r = requests.get(link)
soup = bs(r.content,"lxml")

iyilesen = soup.find_all("span",class_="label label-success text-nowrap")
vefat = soup.find_all("span",class_="label label-danger text-nowrap")
ulke = soup.find_all("a")
yeni_vaka = soup.find_all("span",class_="label label-primary text-nowrap")







liste1 = list()
liste2 = list()
liste3 = list()
liste4 = list()

for i in ulke:
    a = i.find("b")
    if a == None:
        pass
    else:
        liste1.append(a.text)

for a in iyilesen:
    liste2.append(a.text)

print("1.liste doldu")

for b in vefat:
    liste3.append(b.text)


for c in yeni_vaka:
    liste4.append(int(c.text))



a1 = 0
a2 = 0
a3 = 0
a4 = 0
sayi = 0

# Risk ülkesi olmayanlar
analiz1 = list()

# Risk ülkesi olanlar
analiz2 = list()



for ll in liste1:
    sayi += 1

while 0 != sayi:
    sayi -= 1
   
    print("""
    ([Şehir] - [{}])  
    ([İyilesen] - [{}] << Toplam )  
    ([Vefat] - [{}] << Toplam )
    ([Yeni Vaka] - [{}] << Günlük )
    """.format(liste1[a1],liste2[a2],liste3[a3],liste4[a4]))
    a1 += 1
    a2 += 1
    a3 += 1
    a4 += 1
bb = 0
for b in liste4:
    #print(type(a))    
    if b >= 50:
        analiz2.append("Riskli: "+liste1[bb])

    else:                  
        analiz1.append("Risksiz: "+liste1[bb])
    bb += 1



for aa in analiz1:
    print(aa)

print()

for aa in analiz2:
    print(aa)


while True:
    sehir = input("Sorgu Sehir:")
    if "Risksiz: {}".format(sehir) in analiz1:
        print("Risksiz !")
        
    else:
        print("Riskli !")

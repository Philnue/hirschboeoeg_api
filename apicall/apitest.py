
import requests
import csv


#res = requests.get("http://192.168.178.67:7777/loadallmitglieder/")
res = requests.get("http://127.0.0.1:8000/loadalltermine/")
#res2 = requests.get("http://192.168.178.67:7777/loadpersonbyid/3")

#t2 = res2.json()


t = res.json()

if t != None:
    for item in t:
        print(item)
        

#with open("./src/personen.csv") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=';')
#    for i in csv_file:
#       print(i)

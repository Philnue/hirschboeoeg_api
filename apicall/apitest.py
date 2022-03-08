
import requests
import csv



ttt = "äühaslhkdfashdfa"
print(ttt)



#res = requests.get("http://192.168.178.67:7777/loadallmitglieder/")
res = requests.get("http://192.168.178.67:7777/loadalltermine/")
#res = requests.get("http://192.168.178.67:7777/loadallterminabstimmung")
#res2 = requests.get("http://192.168.178.67:7777/loadpersonbyid/3")   /addTerminAbstimmung/{termin_id},{mitglied_id},{entscheidung}

#t2 = res2.json()


t = res.json()

if t != None:
    for item in t:
        print(item)
        

#with open("./src/personen.csv") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=';')
#    for i in csv_file:
#       print(i)

import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime

class BlTermin (BusinesssLogic):

    def getAllTermineSorted(self):
        try:
            print("in blTermin")
            calcDate = str(datetime.today())[0:10]
            command = f"SELECT termin.id, termin.name, datum,adresse,uhrzeit,notizen,treffpunkt,Kleidung.name FROM Termin, Kleidung WHERE Kleidung.id == kleidung_id AND datum >= '{calcDate}' ORDER BY datum, uhrzeit"
            self.execute_command(command)
            s = []
            
            for item in self.cur.fetchall():
                d = {"id": item[0], "name" : item[1], "datum" : item[2],"adresse" : item[3],"uhrzeit" : item[4],"notizen" : item[5],"treffpunkt" : item[6],"kleidung" : item[7]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries sorted: " + str(d.args))

    def getAllTermine(self):

        try:
            command = "SELECT termin.id, termin.name, datum,adresse,uhrzeit,notizen,treffpunkt,Kleidung.name FROM Termin, Kleidung WHERE Kleidung.id == kleidung_id"
            self.execute_command(command)
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "name" : item[1], "datum" : item[2],"adresse" : item[3],"uhrzeit" : item[4],"notizen" : item[5],"treffpunkt" : item[6],"kleidung" : item[7]}
                
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries: " + str(d.args))

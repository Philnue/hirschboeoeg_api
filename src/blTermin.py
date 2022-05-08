import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime

class BlTermin (BusinesssLogic):

    def getAllTermineSorted(self):
        try:
           
            calcDate = str(datetime.today())[0:10]
            
            command = f"SELECT termin.id, termin.name, zeitpunkt,adresse,notizen,treffpunkt,Kleidung.name FROM Termin, Kleidung WHERE Kleidung.id == kleidung_id AND zeitpunkt >= '{calcDate}' ORDER BY zeitpunkt"
            self.execute_command(command)
            s = []
            
            for item in self.cur.fetchall():
                d = {"id": item[0], "name" : item[1], "zeitpunkt" : item[2],"adresse" : item[3],"notizen" : item[4],"treffpunkt" : item[5],"kleidung" : item[6]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries sorted: " + str(d.args))

    def getAllTermine(self):

        try:
            command = "SELECT termin.id, termin.name, zeitpunkt,adresse,uhrzeit,notizen,treffpunkt,Kleidung.name FROM Termin, Kleidung WHERE Kleidung.id == kleidung_id"
            self.execute_command(command)
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "name" : item[1], "zeitpunkt" : item[2],"adresse" : item[3],"notizen" : item[4],"treffpunkt" : item[5],"kleidung" : item[6]}
                
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries: " + str(d.args))

    def getTerminById(self, id):
        try:
            command = "SELECT termin.id, termin.name, zeitpunkt,adresse,uhrzeit,notizen,treffpunkt,Kleidung.name FROM Termin, Kleidung WHERE Kleidung.id == kleidung_id AND termin.id == ?"
            self.execute_command_tuple(command,(id,))
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "name" : item[1], "zeitpunkt" : item[2],"adresse" : item[3],"notizen" : item[4],"treffpunkt" : item[5],"kleidung" : item[6]}
                
                s.append(d)

            return s

        except Exception as d:
            print("Error getting entrie by id: " + str(d.args))

    def createTermin(self, name, zeitpunkt, adresse, kleidung_id, treffpunkt, notizen = "" ):

        try:
            command = "INSERT INTO termin (name, zeitpunkt, adresse, kleidung_id, treffpunkt, notizen) VALUES (?,?,?,?,?,?)"
            self.execute_command_tuple(command,(name,zeitpunkt, adresse,kleidung_id, treffpunkt, notizen))
            self.commit_changes()

            commandCreateAllTA = "INSERT INTO terminabstimmung (termin_id, entscheidung, mitglieder_id) SELECT (SELECT max(id) FROM termin), 0, M.id FROM mitglieder AS M"

            self.execute_command(commandCreateAllTA)
            self.commit_changes()

            command2 = "SELECT max(id) FROM termin"

            self.execute_command(command2)

            return self.cur.fetchall()[0]
            

        except Exception as d:
            print("Error getting entrie by id: " + str(d.args))
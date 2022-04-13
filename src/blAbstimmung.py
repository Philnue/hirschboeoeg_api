import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime



class BlAbstimmung (BusinesssLogic):

    def _getAllAbstimmungen(self):
        try:
            #command = "SELECT id, mitglied_id, erstellungsDatum, erstellungsUhrzeit, frage FROM Abstimmung"

            #command = "SELECT * FROM Abstimmung"
            command = "SELECT Abstimmung.id, Abstimmung.mitglied_id,vorname, nachname, geburtsdatum, erstellungsDatum, erstellungsUhrzeit, frage, titel, ablaufDatum FROM Abstimmung, Mitglieder WHERE Mitglieder.id == Abstimmung.mitglied_id ORDER BY erstellungsDatum"
            self.execute_command(command)
            
            s = []

            for item in self.cur.fetchall():
               
                #d = {"id": item[0], "mitglied_id" : item[1], "erstellungsDatum" : item[2],"erstellungsUhrzeit" : item[3],"frage" : item[4] }
                d = {"Abstimmung.id": item[0], "mitglied_id" : item[1], "vorname" : item[2],"nachname" : item[3],"geburtsdatum" : item[4], "erstellungsDatum" : item[5], "erstellungsUhrzeit" : item[6], "frage" : item[7] , "titel" : item[8], "ablaufDatum" : item[9]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all Abstimmungen: " + str(d.args))

    def _deleteAbstimmungById(self, id):
        try:
            command = "DELETE FROM Abstimmung WHERE id == ?"
            self.execute_command_tuple(command, (id,))
            self.commit_changes()

            return True

        except Exception as d:
            print("Error getting all Abstimmungen: " + str(d.args))
            return False

    def _addTerminAbstimmung(self, mitglied_id, frage, title, ablaufDatum):
        try:

            print(mitglied_id)
            print(title)
            print(frage)
            command = "INSERT INTO Abstimmung (mitglied_id, erstellungsDatum, erstellungsUhrzeit,frage, titel, ablaufDatum) VALUES (?, DATE('now'), TIME('now'), ?, ?, ?)"
            self.execute_command_tuple(command, (mitglied_id,frage, title, ablaufDatum))
            self.commit_changes()

            return True

        except Exception as d:
            print("Error getting all Abstimmungen: " + str(d.args))
            return False

    def _loadSummary(self, abstimmung_id):
        try:
            #SELECT count(entscheidung), entscheidung FROM AbstimmungStimme, Abstimmung WHERE Abstimmung.id == AbstimmungStimme.abstimmungs_id GROUP BY entscheidung
         
            command = "SELECT count(entscheidung), entscheidung FROM AbstimmungStimme, Abstimmung WHERE AbstimmungStimme.abstimmungs_id == ? GROUP BY entscheidung"
 
            self.execute_command_tuple(command, (abstimmung_id,))
            
            s = []

            for item in self.cur.fetchall():
               
              
                d = {"count(entscheidung)": item[0], "entscheidung" : item[1]}
                s.append(d)
            command2 = "SELECT count(*) FROM Mitglieder"

            self.execute_command(command2)
            for item in self.cur.fetchall():
               
              
                d = {"registrierteMitglieder": item[0]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all Abstimmungsstimme: " + str(d.args))
            return False
import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime



class BlAbstimmung (BusinesssLogic):

    def _getAllAbstimmungen(self):
        try:
          
            command = "SELECT Abstimmung.id, Mitglieder.id,vorname, nachname, spitzname, erstellungszeitpunkt, frage, titel, isAnonym FROM Abstimmung, Mitglieder WHERE mitglieder.id == ersteller_id ORDER BY erstellungszeitpunkt"
            print(command)
            self.execute_command(command)
            
            
            s = []

            for item in self.cur.fetchall():
               
                mitgliedList = {"id":item[1],"vorname":item[2],"nachname":item[3],"spitzname":item[4]}
                abstimmungsList = {"id":item[0],"erstellungszeitpunkt":item[5],"frage":item[6],"titel":item[7], "isAnonym":item[8]}

                d = {"mitglied":mitgliedList, "abstimmung":abstimmungsList}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all Abstimmungen: " + str(d.args))

    def _deleteAbstimmungById(self, id):
        try:
            command = "DELETE FROM abstimmung WHERE id == ?"
            self.execute_command_tuple(command, (id,))
            self.commit_changes()

            return True

        except Exception as d:
            print("Error getting all Abstimmungen: " + str(d.args))
            return False

    def _addAbstimmung(self, mitglied_id, frage, title, isAnonym):
        try:

            command = "INSERT INTO Abstimmung (ersteller_id, frage, titel,erstellungszeitpunkt, isAnonym) VALUES (?, ?, ?, DATETIME('now'),?)"

            commandCreateAllTA = "INSERT INTO abstimmungsstimme (abstimmung_id, entscheidung, mitglieder_id) SELECT (SELECT max(id) FROM abstimmung), 0, M.id FROM mitglieder AS M"


            self.execute_command_tuple(command, (mitglied_id,frage, title))
            self.commit_changes()

            self.execute_command(commandCreateAllTA)
            self.commit_changes()

            return True

        except Exception as d:
            print("Error getting all Abstimmungen: " + str(d.args))
            return False

    

    def _loadSummary(self, abstimmung_id):
        try:
            #SELECT count(entscheidung), entscheidung FROM AbstimmungStimme, Abstimmung WHERE Abstimmung.id == AbstimmungStimme.abstimmungs_id GROUP BY entscheidung
         
            command = "SELECT count(entscheidung) as anzahl, entscheidung FROM AbstimmungStimme WHERE abstimmung_id == ? GROUP BY entscheidung"
 
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
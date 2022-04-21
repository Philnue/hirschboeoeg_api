from operator import truediv
import sqlite3
from sqlite3 import Error
from tkinter import E
from xml.etree.ElementTree import TreeBuilder
from xmlrpc.client import DateTime
from helper.mitlied import Mitglied
from datetime import date, datetime

class BusinesssLogic():
    
    def __init__(self):
        try:
            self.con = sqlite3.connect("../Database/hirschboeoeg.db")
            self.cur = self.con.cursor()
            print("Database connection: connected")
        except Exception as e:
            print("Database connection: Error connecting: " + str(e.args))
            return False
   

    def add_termin_abstimmung(self, termin_id, mitglied_id, entscheidung):
        try:
            command = "INSERT INTO TerminAbstimmung (termin_id, entscheidung, mitglieder_id) VALUES (?,?,?)"
            print(command)
            self.execute_command_tuple(command, (termin_id,entscheidung, mitglied_id))
            self.commit_changes()
            print("Added Termin abstimmung: {termin_id} {entscheidung} {mitglied_id}")
            return True
        except Exception as e:
            print("Database connection: Error getting item by id" + str(e))
            return False

    def load_all_termin_zusagen_by_terminid(self, termin_id):
        try:

            command = "SELECT Mitglieder.id, Mitglieder.vorname, Mitglieder.nachname, Mitglieder.spitzName FROM TerminAbstimmung, Mitglieder WHERE Mitglieder.id == TerminAbstimmung.mitglieder_id AND TerminAbstimmung.termin_id == ? AND entscheidung == 1"

            self.execute_command_tuple(command,(termin_id,))
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0],"vorname": item[1], "nachname" : item[2], "spitzName" : item[3]}
                s.append(d)

            return s
        except Exception as e:
            print("Database connection: Error getting item by id" + str(e))
            return False

    def loadCounts(self, termin_id):
        try:

            command = "SELECT entscheidung, COUNT(*) as anzahl FROM TerminAbstimmung, Mitglieder WHERE Mitglieder.id == TerminAbstimmung.mitglieder_id AND termin_id == ? GROUP BY entscheidung"

            self.execute_command_tuple(command,(termin_id,))
            s = []

            for item in self.cur.fetchall():
                d = {"entscheidung": item[0],"anzahl": item[1]}
                s.append(d)


            command2 = "SELECT count(*) FROM Mitglieder"

            self.execute_command(command2)
            for item in self.cur.fetchall():
               
                d = {"registrierteMitglieder": item[0]}
                s.append(d)
            return s
        except Exception as e:
            print("Database connection: Error getting item by id" + str(e))
            return False


   

    def execute_command(self,command):
        self.cur.execute(command)
    
    def execute_command_tuple(self,command, tuple):
        self.cur.execute(command, tuple)
    
    def commit_changes(self):
        self.con.commit()

    def print_database_error(self,command, error_message = "Database connection", ):
        return (error_message + str(command))

    def getAllTerminAbstimmung(self):

        try:
            command = "SELECT id, mitglieder_id, termin_id, entscheidung FROM TerminAbstimmung"
            self.execute_command(command)
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "mitglieder_id" : item[1], "termin_id" : item[2],"entscheidung" : item[3]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries: " + str(d.args))
            return False


    def deleteTerminAbstimmungByMitgliedAndTermin(self, mitgliedId, terminId):

        try:
            command = "DELETE FROM TerminAbstimmung WHERE termin_id == ? AND mitglieder_id == ?"
            self.execute_command_tuple(command, (terminId, mitgliedId))
            print(command)
            self.commit_changes()

           
            print("Deleted item with MG {mitgliedId} Termin {terminId}")
            return True

        except Exception as d:
            print("Error getting all entries: " + str(d.args))
            return False

    def getTerminAbstimmungByMitgliedIdAndTerminId(self, mitgliedId, terminId):

        try:
            command = "SELECT entscheidung FROM TerminAbstimmung WHERE termin_id == ? AND mitglieder_id == ?"
            self.execute_command_tuple(command, (terminId, mitgliedId))
            s = []

            for item in self.cur.fetchall():
                d = {"entscheidung": item[0]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries: " + str(d.args))
            return False

    def updateTerminAbstimmungByMitgliedIdAndTerminId(self, mitgliedId, terminId, entscheidung):

        try:
            command = "UPDATE TerminAbstimmung SET entscheidung = ? WHERE termin_id == ? AND mitglieder_id == ?"
            self.execute_command_tuple(command, (entscheidung, terminId, mitgliedId))
            self.commit_changes()


            return True

        except Exception as d:
            print("Error getting all entries: " + str(d.args))
            return False

    
    
    def verifiyLicense(self, license):
        try:
            command = "SELECT id, license, amount FROM Lizenz WHERE license == ?"
            self.execute_command_tuple(command, (license,))
            
            s = []
            verified = False

            for item in self.cur.fetchall():
                d = {"id": item[0], "license" : item[1], "amount": item[2]}
                print(d)
                print(item[2])
                if int(item[2]) > 0:
                    verified = True
                    new_amount = item[2] - 1
                    command = "UPDATE Lizenz SET amount = ? WHERE id == ?"
                    self.execute_command_tuple(command, (new_amount, item[0]))
                    self.commit_changes()
                    
                
            return verified

        except Exception as d:
            print("Error getting license: " + str(d.args))
            return False

    def loadAllnews(self):
        try:
            command = "SELECT id, erstellungsDatum, neuigkeit FROM News ORDER BY erstellungsDatum DESC"
            self.execute_command(command)
            
            s = []
            for item in self.cur.fetchall():
                d = {"id": item[0], "erstellungsDatum" : item[1], "neuigkeit": item[2]}
               
                s.append(d)
                    
                
            return s

        except Exception as d:
            print("Error getting all News: " + str(d.args))
            return False

   
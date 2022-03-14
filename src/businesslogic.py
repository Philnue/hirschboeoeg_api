from operator import truediv
import sqlite3
from sqlite3 import Error
from tkinter import E
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
   

    def add_termin_abstimmung(self, termin_id, mitglied_id, entscheidung):
        try:
            command = "INSERT INTO TerminAbstimmung (termin_id, entscheidung, mitglieder_id) VALUES (?,?,?)"
            print(command)
            self.execute_command_tuple(command, (termin_id,entscheidung, mitglied_id))
            self.commit_changes()
            return f"Added Termin abstimmung: {termin_id} {entscheidung} {mitglied_id}"
        except Exception as e:
            print("Database connection: Error getting item by id" + str(e))

    def load_all_termin_zusagen_by_terminid(self, termin_id):
        try:

            command = "SELECT Mitglieder.vorname, Mitglieder.nachname FROM TerminAbstimmung, Mitglieder WHERE Mitglieder.id == TerminAbstimmung.id AND Termin.id == ?"

            self.execute_command_tuple(command,(termin_id,))
            s = []

            for item in self.cur.fetchall():
                d = {"vorname": item[0], "nachname" : item[1]}
                s.append(d)

            return s
        except Exception as e:
            print("Database connection: Error getting item by id" + str(e))


   

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


    def deleteTerminAbstimmungByMitgliedAndTermin(self, mitgliedId, terminId):

        try:
            command = "DELETE FROM TerminAbstimmung WHERE termin_id == ? AND mitglieder_id == ?"
            self.execute_command_tuple(command, (terminId, mitgliedId))
            print(command)
            self.commit_changes()

           
            return f"Deleted item with MG {mitgliedId} Termin {terminId}"

        except Exception as d:
            print("Error getting all entries: " + str(d.args))

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

    def updateTerminAbstimmungByMitgliedIdAndTerminId(self, mitgliedId, terminId, entscheidung):

        try:
            command = "UPDATE TerminAbstimmung SET entscheidung = ? WHERE termin_id == ? AND mitglieder_id == ?"
            self.execute_command_tuple(command, (entscheidung, terminId, mitgliedId))
            self.commit_changes()


            return "true"

        except Exception as d:
            print("Error getting all entries: " + str(d.args))
            return "false"

    
    
    

    
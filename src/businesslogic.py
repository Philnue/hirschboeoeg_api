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
            self.execute_command_tuple(command, (termin_id,entscheidung, mitglied_id))
            self.commit_changes()
            return f"Added Termin abstimmung: {termin_id} {entscheidung} {mitglied_id}"
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
            command = "SELECT * FROM TerminAbstimmung"
            self.execute_command(command)
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "mitgliedid" : item[1], "terminId" : item[2],"entscheidung" : item[3]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries: " + str(d.args))

    
    
    

    
import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from helper.mitlied import Mitglied
from datetime import date, datetime

class BusinesssLogic():
    
    def __init__(self):
        try:
            self.con = sqlite3.connect("../../Database/hirschboeoeg.db")
            self.cur = self.con.cursor()
            print("Database connection: connected")
        except Exception as e:
            print("Database connection: Error connecting: " + str(e.args))

    def get_item_by_id(self, id):
        try:
            command = "SELECT * FROM Personen where id == ?"
            self.execute_command_tuple(command, (id,))
            p = self.cur.fetchone()
            return p
        except Exception as e:
            print("Database connection: Error getting item by id" + str(e))

    def getAllMitglieder(self):

        try:
            command = "SELECT * FROM Mitglieder"
            self.execute_command(command)
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "vorname" : item[1], "nachname" : item[2],"geb" : item[3]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries: " + str(d.args))


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

    def getAllTermineSorted(self):
        try:
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


    def insert_into(self, vorname, nachname):

        try:
            command = "INSERT INTO Personen (Vorname, Nachname) VALUES (?,?)"
            self.execute_command_tuple(command, (vorname,nachname))
            self.commit_changes()
            return f"Added Person: {vorname} {nachname}"
        except Exception as e:
            return( "Adding person error" + str(e.args))

    def delete_by_id(self, id):
        try:
            command = "DELETE FROM Personen WHERE id == ?"
            self.execute_command_tuple(command, (id,))
            self.commit_changes()
            return f"Deleted person with id {id}"
        except Exception as e:
            return ("Delete error" + str(e))

    def execute_command(self,command):
        self.cur.execute(command)
    
    def execute_command_tuple(self,command, tuple):
        self.cur.execute(command, tuple)
    
    def commit_changes(self):
        self.con.commit()

    def print_database_error(self,command, error_message = "Database connection", ):
        return (error_message + str(command))
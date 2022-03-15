import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime



class BlAbstimmung (BusinesssLogic):

    def _getAllAbstimmungen(self):
        try:
            command = "SELECT id, mitglied_id, erstellungsDatum, frage FROM Abstimmung"
            self.execute_command(command)
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "mitglied_id" : item[1], "erstellungsDatum" : item[2],"frage" : item[3]}
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

    def _addTerminAbstimmung(self, mitglied_id, frage):
        try:
            command = "INSERT INTO Abstimmung (mitglied_id, erstellungsDatum, erstellungsUhrzeit,frage) VALUES (?, DATE('now'), TIME('now'), ?)"
            self.execute_command_tuple(command, (mitglied_id,frage))
            self.commit_changes()

            return True

        except Exception as d:
            print("Error getting all Abstimmungen: " + str(d.args))
            return False
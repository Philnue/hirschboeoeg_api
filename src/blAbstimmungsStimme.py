import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime



class BlAbstimmungsStimme (BusinesssLogic):
    pass

    def _addAbstimmungsStimme(self,mitglied_id, abstimmungs_id, entscheidung):
        
        try:
            command = "INSERT INTO Abstimmung (mitglied_id, erstellungsDatum, erstellungsUhrzeit,frage) VALUES (?, DATE('now'), TIME('now'), ?)"
            self.execute_command_tuple(command, (mitglied_id,abstimmungs_id, entscheidung))
            self.commit_changes()

            return True

        except Exception as d:
            print("Error adding abstimmungsstimme: " + str(d.args))
            return False
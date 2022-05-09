import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime



class BlAbstimmungsStimme (BusinesssLogic):
        
    def _addAbstimmungsStimme(self,mitglied_id, abstimmungs_id, entscheidung):
        
        try:
            command = "INSERT INTO AbstimmungStimme (mitglied_id, stimmenDatum, stimmenUhrzeit,abstimmung_id, entscheidung) VALUES (?, DATE('now'), TIME('now'), ?, ?)"
            self.execute_command_tuple(command, (mitglied_id,abstimmungs_id, entscheidung))
            self.commit_changes()

            return True

        except Exception as d:
            print("Error adding abstimmungsstimme: " + str(d.args))
            return False

    def _setAbstimmungsStimme(self,mitglieder_id, abstimmung_id, entscheidung):
        
        try:
            command = "UPDATE abstimmungsstimme SET entscheidung = ? WHERE mitglieder_id == ? AND abstimmung_id == ?"
            print(command)
            self.execute_command_tuple(command, (entscheidung,mitglieder_id, abstimmung_id))
            self.commit_changes()

            return True

        except Exception as d:
            print("Error update abstimmungsstimme: " + str(d.args))
            return False


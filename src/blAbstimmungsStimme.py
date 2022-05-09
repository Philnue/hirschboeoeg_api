import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime
import newMitglieder as dbNewMitglieder


conNewMitglieder = dbNewMitglieder.NewBlMitglieder()


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

    def _loadAbstimmungsStimme(self, abstimmung_id):

        try:
            command = "SELECT abstimmung.id,abstimmung.frage,abstimmung.titel,abstimmung.erstellungszeitpunkt,abstimmung.isAnonym,abstimmung.ersteller_id,mitglieder.id,mitglieder.vorname,mitglieder.nachname,mitglieder.spitzname,entscheidung,FROM abstimmungsstimme LEFT JOIN abstimmung ON abstimmung.id==abstimmungsstimme.abstimmung_id LEFT JOIN mitglieder ON mitglieder.id==abstimmungsstimme.mitglieder_id WHERE abstimmung_id==?"
            print(command)
            self.execute_command_tuple(command, (abstimmung_id,))
            
            list = []
            for item in self.cur.fetchall():
                abstimmung = {"id":item[0],"frage":item[1],"titel":item[2],"erstellungszeitpunkt":item[3],"isAnonym":item[4],"ersteller_id":item[5]}

                mitglied = {"id" : item[6],"vorname" : item[7],"nachname" : item[8],"spitzname" : item[9]}

                ersteller = conNewMitglieder._getMitgliedById(item[5])

                t = {"abstimmung" :abstimmung, "mitglied": mitglied,"ersteller": ersteller, "entscheidung": item[10]}
                list.append(t)

            return True

        except Exception as d:
            print("Error update abstimmungsstimme: " + str(d.args))
            return False

    #SELECT*FROM abstimmungsstimme LEFT JOIN abstimmung ON abstimmung.id==abstimmungsstimme.abstimmung_id LEFT JOIN mitglieder on mitglieder.id==abstimmungsstimme.mitglieder_id WHERE abstimmung_id==1


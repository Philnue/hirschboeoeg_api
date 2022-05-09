from operator import truediv
import sqlite3
from sqlite3 import Error
from xmlrpc.client import DateTime
from businesslogic import BusinesssLogic
from helper.mitlied import Mitglied
from datetime import date, datetime



class BlMitglieder (BusinesssLogic):


    def _getAllMitglieder(self):

        try:
            command = "SELECT * FROM Mitglieder"
            self.execute_command(command)
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "vorname" : item[1], "nachname" : item[2], "spitzname":item[3]}
                s.append(d)

            return s

        except Exception as d:
            print("Error getting all entries: " + str(d.args))

    def _getMitgliederIdByName(self, vorname, nachname):
        try: 
            command = "SELECT id FROM Mitglieder WHERE vorname == ? and nachname == ?"
            self.execute_command_tuple(command, (vorname,nachname))
            s = []

            for item in self.cur.fetchall():
                d = {"id" : item[0]}
                s.append(d)
            return s

        except Exception as e:
            print(str(e.args))

    def _getFullMitgliedIdByName(self, vorname, nachname):
        try: 
            command = "SELECT id, vorname, nachname, spitzname FROM Mitglieder WHERE vorname == ? and nachname == ?"
            self.execute_command_tuple(command, (vorname,nachname))
            s = []

            for item in self.cur.fetchall():
               d = {"id": item[0], "vorname" : item[1], "nachname" : item[2],"spitzname":item[3]}
               s.append(d)

            return s

        except Exception as e:
            print(str(e.args))

    def _updateMitgliedWithId(self,id, vorname, nachname):
        try: 
            command = "UPDATE Mitglieder SET vorname = ?, nachname = ? WHERE Mitglieder.id == ?"
            self.execute_command_tuple(command, (vorname,nachname, id))
            self.commit_changes()

            
            return True

        except Exception as e:
            print(str(e.args))
            return False


    def _addMitgliedWithoutGeburtstag(self, vorname, nachname):
        try: 
            #! Add Mitglied TA automatisch
            t = self._getMitgliederIdByName(vorname, nachname)

            if len(t) == 1:
                print(len(t))
                return t
            else:

                command = "INSERT INTO Mitglieder (vorname, nachname) VALUES (?,?)"
                self.execute_command_tuple(command, (vorname,nachname))
                self.commit_changes()
                t = self._getMitgliederIdByName(vorname, nachname)
                return t
            
        except Exception as e:
            print(str(e.args))
            return False

    def _getMitgliedById(self, id):
        try: 
            command = "SELECT id, vorname, nachname, spitzname FROM Mitglieder WHERE id == ?"
            self.execute_command_tuple(command, (id,))
            self.commit_changes()
            s = []

            for item in self.cur.fetchall():
                d = {"id": item[0], "vorname" : item[1], "nachname" : item[2],"spitzname":item[3] }
                s.append(d)
            return s

        except Exception as e:
            print(str(e.args))

    def _addShortName(self, mitglied_id, shortName ):
        try: 
            command = "UPDATE Mitglieder SET spitzname = ? WHERE id == ?"
            self.execute_command_tuple(command, (shortName,mitglied_id))
            self.commit_changes()
           
            return True

        except Exception as e:
            print(str(e.args))
            return False

    def _updateShortName(self, mitglied_id, shortName ):
        try: 
            command = "UPDATE Mitglieder SET spitzname = ? WHERE id == ?"
            self.execute_command_tuple(command, (shortName,mitglied_id))
            self.commit_changes()
           
            return True

        except Exception as e:
            print(str(e.args))
            return False
    def _deleteShortname(self, mitglied_id ):
        try: 
            command = "UPDATE Mitglieder SET spitzname = null WHERE id == ?"
            self.execute_command_tuple(command, (mitglied_id,))
            self.commit_changes()
           
            return True

        except Exception as e:
            print(str(e.args))
            return False
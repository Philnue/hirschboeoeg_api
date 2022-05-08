from re import L
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)

        cursor = conn.cursor()

        #cursor.execute("""CREATE TABLE IF NOT EXISTS termin ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [name] Text, [zeitpunkt] Datetime, [adresse] Text, [notizen] Text, [kleidung_id] INTEGER, [treffpunkt] Text, FOREIGN KEY (kleidung_id) REFERENCES kleidung (id))""")
        #cursor.execute("""INSERT INTO termin (name, zeitpunkt, adresse, notizen, kleidung_id, treffpunkt) VALUES ("name1", "2020-03-20 03:02", "adresse", "notizen", 1, "treff")""")
        #cursor.execute("""SELECT * FROM Termin CROSS JOIN Kleidung ON Termin.kleidung_id == kleidung.id""")
        #cursor.execute("""INSERT INTO mitglieder (vorname, nachname) VALUES ("vorname2","nachname2")""")
        #cursor.execute("""SELECT * FROM mitglieder""")
        #cursor.execute("""CREATE TABLE terminabstimmung ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [termin_id] INTEGER NOT NULL, [mitglieder_id] INTEGER NOT NULL, [entscheidung] INTEGER, FOREIGN KEY (termin_id) REFERENCES termin (id), FOREIGN KEY (mitglieder_id) REFERENCES mitglieder (id))""")
        #cursor.execute("""INSERT INTO terminabstimmung (termin_id, mitglieder_id, entscheidung) VALUES (1,1,1)""")
        ##cursor.execute("""SELECT * FROM terminabstimmung JOIN termin on termin.id == terminabstimmung.termin_id FULL JOIN mitglieder on mitglieder.id == terminabstimmung.mitglieder_id WHERE mitglieder_id == 1""")
        #cursor.execute("""INSERT INTO terminabstimmung (termin_id, entscheidung, mitglieder_id) SELECT T.id, 0, 24 FROM termin AS T""")
        cursor.execute("""SELECT Termin.id AS termin_id,Termin.name ,termin.zeitpunkt,termin.adresse,termin.notizen,termin.kleidung_id,termin.treffpunkt,mitglieder.id AS mitglieder_id, mitglieder.vorname,mitglieder.nachname,Mitglieder.spitzname,entscheidung,kleidung.name,kleidung.id FROM TerminAbstimmung JOIN Termin ON Termin.id==TerminAbstimmung.termin_id JOIN Mitglieder ON Mitglieder.id==TerminAbstimmung.mitglieder_id JOIN kleidung ON kleidung.id==kleidung_id WHERE mitglieder_id==1 ORDER BY zeitpunkt""")
        list = []
        for item in cursor.fetchall():
            termin = {"id" : item[0], "name" : item[1],"zeitpunkt" : item[2],"adresse" : item[3], "notizen" : item[4], "kleidung" : item[12],"treffpunkt" : item[6]}
            mitglied = {"id" : item[7],"vorname" : item[8],"nachname" : item[9],"spitzname" : item[10]}


            t = {"mitglied" :mitglied, "termin": termin, "entscheidung": item[11]}
            list.append(t)

        print(list)
        #! NeuerTermin Befehl
        #! Automatisch 
        #! INSERT INTO TerminAbstimmung (termin_id, entscheidung, mitglieder_id) SELECT (SELECT max(id) FROM Termin), 0, M.id FROM Mitglieder AS M;

        print(cursor.fetchall())

        conn.commit()
        
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection("Database/test.db")
from os import system
import os
from sqlite3 import dbapi2
from typing import ItemsView
from fastapi import FastAPI
import businesslogic as dbConnection
import blTermin as dbConnectionTermine
import blMitglieder as dbConnectionMitglieder
import json

#   in src wechseln zum starate 
#   uvicorn main:api --reload

api = FastAPI()
con = dbConnection.BusinesssLogic()
conTermine = dbConnectionTermine.BlTermin()
conMitglieder = dbConnectionMitglieder.BlMitglieder()

@api.get("/")
async def root():
    return "Hey na du"



@api.get("Termine/loadalltermine/")
async def get_all_items():
    values = conTermine.getAllTermineSorted()
    return values

@api.get("TerminAbstimmung/addTerminAbstimmung/{termin_id},{mitglied_id},{entscheidung}")
async def addTerminAbstimmung(termin_id, mitglied_id, entscheidung):
    return con.add_termin_abstimmung(termin_id, mitglied_id, entscheidung)

@api.get("TerminAbstimmung/loadallterminabstimmung/")
async def get_all_termin_abstimmung():
    values = con.getAllTerminAbstimmung()
    #command
    return values



#Mitglieder

@api.get("Mitglieder/getMitgliedById/{vorname},{nachname}")
async def create_item(vorname, nachname):
    return conMitglieder._getMitgliederIdByName(vorname, nachname)

@api.get("Mitglieder/addMitglied/{vorname},{nachname}")
async def create_item(vorname, nachname):
    return conMitglieder._addMitgliedWithoutGeburtstag(vorname, nachname)

@api.get("Mitglieder/loadallmitglieder/")
async def get_all_items():
    values = conMitglieder._getAllMitglieder()
    return values

@api.get("Mitglieder/updatemitgliedwithid/{vorname},{nachname}")
async def get_all_items(vorname,nachname):
    values = conMitglieder._updateMitgliedWithId(vorname,nachname)
    return values
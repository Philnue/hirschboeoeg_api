from os import system
import os
from sqlite3 import dbapi2
from typing import ItemsView
from fastapi import FastAPI
import businesslogic as dbConnection
import blTermin as dbConnectionTermine
import blMitglieder as dbConnectionMitglieder
import blAbstimmung as dbAbstimmungen
import blAbstimmungsStimme as dbAbstimmungsStimme
import json

#   in src wechseln zum starate 
#   uvicorn main:api --reload

api = FastAPI()
con = dbConnection.BusinesssLogic()
conTermine = dbConnectionTermine.BlTermin()
conMitglieder = dbConnectionMitglieder.BlMitglieder()
conAbstimmungen = dbAbstimmungen.BlAbstimmung()
conAbstimmungsStimme = dbAbstimmungsStimme.BlAbstimmungsStimme()

@api.get("/")
async def root():
    return "Hey na du"


@api.get("/Termine/loadalltermine/")
async def get_all_items():
   
    values = conTermine.getAllTermineSorted()
    return values

@api.get("/TerminAbstimmung/addTerminAbstimmung/{termin_id},{mitglied_id},{entscheidung}")
async def addTerminAbstimmung(termin_id, mitglied_id, entscheidung):
    return con.add_termin_abstimmung(termin_id, mitglied_id, entscheidung)

@api.get("/TerminAbstimmung/loadAllTerminZusagenByTerminId/{termin_id}")
async def addTerminAbstimmung(termin_id):
    return con.load_all_termin_zusagen_by_terminid(termin_id)

@api.get("/TerminAbstimmung/loadallterminabstimmung/")
async def get_all_termin_abstimmung():
    values = con.getAllTerminAbstimmung()
    #command
    return values

@api.get("/TerminAbstimmung/loadterminabstimmungbyterminidandmitgliedid/{mitgliedId},{terminId}")
async def get_all_termin_abstimmung(mitgliedId,terminId):
    values = con.getTerminAbstimmungByMitgliedIdAndTerminId(mitgliedId,terminId)
    #command
    return values

@api.get("/TerminAbstimmung/deleteterminabstimmung/{mitgliedId},{terminId}")
async def get_all_termin_abstimmung(mitgliedId,terminId):
    values = con.deleteTerminAbstimmungByMitgliedAndTermin(mitgliedId,terminId)
    #command
    return values

@api.get("/TerminAbstimmung/updateterminabstimmungbyterminidandmitgliedid/{mitgliedId},{terminId},{entscheidung}")
async def get_all_termin_abstimmung(mitgliedId,terminId, entscheidung):
    values = con.updateTerminAbstimmungByMitgliedIdAndTerminId(mitgliedId,terminId,entscheidung)
    #command
    return values



#Mitglieder

@api.get("/Mitglieder/getMitgliedById/{vorname},{nachname}")
async def create_item(vorname, nachname):
    return conMitglieder._getMitgliederIdByName(vorname, nachname)

@api.get("/Mitglieder/getFullMitgliedById/{id}")
async def create_item(id):
    return conMitglieder._getMitgliedById(id)

@api.get("/Mitglieder/addMitglied/{vorname},{nachname}")
async def create_itemT(vorname, nachname):
    return conMitglieder._addMitgliedWithoutGeburtstag(vorname, nachname)

@api.get("/Mitglieder/loadallmitglieder/")
async def get_all_itemsTT():
    values = conMitglieder._getAllMitglieder()
    return values

@api.get("/Mitglieder/updatemitgliedwithid/{id},{vorname},{nachname}")
async def get_all_itemsTTT(id,vorname,nachname):
    values = conMitglieder._updateMitgliedWithId(id,vorname,nachname)
    return values

# Abstimmung

@api.get("/Abstimmung/getAllAbstimmungen/")
async def get_all_abstimmungen():
    return conAbstimmungen._getAllAbstimmungen()

@api.get("/Abstimmung/deleteAbstimmungById/{id}")
async def get_all_abstimmungen(id):
    return conAbstimmungen._deleteAbstimmungById(id)

@api.get("/Abstimmung/addAbstimmung/{mitglied_id},{frage},{title}")
async def get_all_abstimmungen(self, mitglied_id, frage,title):
    return conAbstimmungen._addTerminAbstimmung(mitglied_id, frage,title)

#AbstimmungsStimme

@api.get("/AbstimmungsStimme/addAbstimmungsStimme/{mitglied_id},{abstimmungs_id},{entscheidung}")
async def get_all_abstimmungen(mitglied_id, abstimmungs_id, entscheidung):
    return conAbstimmungsStimme._addAbstimmungsStimme(mitglied_id, abstimmungs_id, entscheidung)
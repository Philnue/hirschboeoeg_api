from os import system
import os
from sqlite3 import dbapi2
from typing import ItemsView
from fastapi import FastAPI
import businesslogic as dbConnection
import blTermin as dbConnectionTermine
import blMitglieder as dbConnectionMitglieder
import blAbstimmung as dbAbstimmungen
import newMitglieder as dbNewMitglieder
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
conNewMitglieder = dbNewMitglieder.NewBlMitglieder()

@api.get("/")
async def root():
    return "Hey na du"

@api.get("/new/addMitglied/")
async def get_all_items():
    #values = conNewMitglieder._addMitgliedWithoutGeburtstag("philipp","testNeuNeu")
    return values

@api.get("/new/addTermin/")
async def get_all_items():
    #values = conTermine.createTermin("testneu", "2022-04-15", "adresse", 1, "treff", "keine notizen")
    return values

@api.get("/new/loadTerminEntscheidung/")
async def get_all_items():
    #!testen
    values = con.loadTerminAbstimmungNewAll()
    return values

@api.get("/new/loadTerminEntscheidungAfterTerminId/{id}")
async def get_all_items(id):
    #!testen
    values = con.loadTerminAbstimmungNewByTerminid(id)
    return values

@api.get("/new/loadTerminEntscheidungAfterMId/{id}")
async def get_all_items(id):
    #!testen
    values = con.loadTerminAbstimmungNewByMId(id)
    return values

@api.get("/Termine/loadalltermine/")
async def get_all_items():
   
    values = conTermine.getAllTermineSorted()
    return values

@api.get("/Termine/loadTerminById/{termin_id}")
async def get_all_items(termin_id):
    return conTermine.getTerminById(termin_id)


    
#Update einbauen dass man sieht wer zu und absagt
@api.get("/TerminAbstimmung/addTerminAbstimmung/{termin_id},{mitglied_id},{entscheidung}")
async def addTerminAbstimmung(termin_id, mitglied_id, entscheidung):
    return con.add_termin_abstimmung(termin_id, mitglied_id, entscheidung)

@api.get("/TerminAbstimmung/loadAllTerminZusagenByTerminId/{termin_id}")
async def addTerminAbstimmung(termin_id):
    return con.load_all_termin_zusagen_by_terminid(termin_id)


@api.get("/TerminAbstimmung/loadCounts/{termin_id}")
async def addTerminAbstimmung(termin_id):
    return con.loadCounts(termin_id)

@api.get("/TerminAbstimmung/loadAllTerminAbstimmungeListByTerminId/{termin_id}")
async def addTerminAbstimmung(termin_id):
    return con.loadAllTerminAbstimmungenByTerminId(termin_id)


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

#rein
#@api.get("/Mitglieder/getMitgliedById/{vorname},{nachname}")
#async def create_item(vorname, nachname):
#    return conMitglieder._getMitgliederIdByName(vorname, nachname)
#rein
#@api.get("/Mitglieder/getFullMitgliedByName/{vorname},{nachname}")
#async def create_item(vorname, nachname):
#    return conMitglieder._getFullMitgliedIdByName(vorname, nachname)

@api.get("/Mitglieder/getMitgliedById/{vorname},{nachname}")
async def create_item(vorname, nachname):
    return conNewMitglieder._getMitgliederIdByName(vorname, nachname)

@api.get("/Mitglieder/getFullMitgliedByName/{vorname},{nachname}")
async def create_item(vorname, nachname):
    return conNewMitglieder._getFullMitgliedIdByName(vorname, nachname)


#wieder rein
#@api.get("/Mitglieder/getFullMitgliedById/{id}")
#async def create_item(id):
#    return conMitglieder._getMitgliedById(id)

@api.get("/Mitglieder/getFullMitgliedById/{id}")
async def create_item(id):
    return conNewMitglieder._getMitgliedById(id)

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

@api.get("/Mitglieder/addShortName/{mitglied_id},{shortName}")
async def get_all_itemsTTT(mitglied_id,shortName):
    values = conMitglieder._addShortName(mitglied_id, shortName)
    return values

@api.get("/Mitglieder/updateShortname/{mitglied_id},{shortName}")
async def get_all_itemsTTT(mitglied_id,shortName):
    values = conMitglieder._updateShortName(mitglied_id, shortName)
    return values

@api.get("/Mitglieder/deleteShortname/{mitglied_id}")
async def get_all_itemsTTT(mitglied_id):
    values = conMitglieder._deleteShortname(mitglied_id)
    return values

# Abstimmung

@api.get("/Abstimmung/getAllAbstimmungen/")
async def get_all_abstimmungen():
    return conAbstimmungen._getAllAbstimmungen()

@api.get("/Abstimmung/deleteAbstimmungById/{id}")
async def get_all_abstimmungen(id):
    return conAbstimmungen._deleteAbstimmungById(id)


@api.get("/Abstimmung/summary/{id}")
async def get_all_abstimmungen(id):
    return conAbstimmungen._loadSummary(id)


@api.get("/Abstimmung/addAbstimmung/{mitglied_id}/{frage}/{title}/{isAnonyn}")
async def get_all_abstimmungen( mitglied_id, frage,title, isAnonyn):
    return conAbstimmungen._addAbstimmung(mitglied_id, frage, title,isAnonyn)

#AbstimmungsStimme

@api.get("/AbstimmungsStimme/addAbstimmungsStimme/{mitglied_id},{abstimmungs_id},{entscheidung}")
async def get_all_abstimmungen(mitglied_id, abstimmungs_id, entscheidung):
    return conAbstimmungsStimme._addAbstimmungsStimme(mitglied_id, abstimmungs_id, entscheidung)


#lizenz

@api.get("/Lizens/verifylicense/{license}")
async def get_all_abstimmungen(license):
    return con.verifiyLicense(license)

# News

@api.get("/Neuigkeiten/loadAllNews/")
async def get_all_abstimmungen():
    return con.loadAllnews()
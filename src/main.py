from os import system
import os
from typing import ItemsView
from fastapi import FastAPI
import businesslogic as dbConnection
import json

#   in src wechseln zum starate 
#   uvicorn main:api --reload

api = FastAPI()
con = dbConnection.BusinesssLogic()

@api.get("/")
async def root():
    return "Hey na du"

@api.get("/loadpersonbyid/{item_id}")
async def read_item(item_id):
    return con.get_item_by_id(item_id)

@api.get("/loadallmitglieder/")
async def get_all_items():
    values = con.getAllMitgliederWithDate()
    return values

@api.get("/loadalltermine/")
async def get_all_items():
    values = con.getAllTermineSorted()
    return values

@api.get("/addTerminAbstimmung/{termin_id},{mitglied_id},{entscheidung}")
async def addTerminAbstimmung(termin_id, mitglied_id, entscheidung):
    return con.add_termin_abstimmung(termin_id, mitglied_id, entscheidung)

@api.get("/addperson/{vorname},{nachname}")
async def create_item(vorname, nachname):
    
    return con.insert_into(vorname, nachname)

import json


import json

class Mitglied():

    def __init__(self, j):
        self.__dict__ = json.loads(j)
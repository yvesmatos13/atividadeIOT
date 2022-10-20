from pymongo import MongoClient

class conexao():

    def __init__(self, colecao):
        self.colecao = colecao

    def iotDS(self):
        cliente = MongoClient('mongodb://172.17.0.2:27017/')
        database = cliente['iot']
        return database[self.colecao]
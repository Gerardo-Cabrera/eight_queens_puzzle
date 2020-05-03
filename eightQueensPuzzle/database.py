#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlalchemy as db


class Database():
    usr = 'postgres'
    passw = '12345678'
    serv = 'localhost'
    db_name = 'eight_queens_puzzle'
    url_db = 'postgresql://{user}:{password}@{server}/{database}'.format(user=usr, password=passw, server=serv, database=db_name)
    engine = db.create_engine(url_db)

    def __init__(self):
        try:
            self.connection = self.engine.connect()
            self.table = 'soluciones'
        except Exception as error:
            print("Ocurrió un error conectando a la base de datos: " + str(error))
    
    def saveData(self, data):
        try:
            self.connection.execute(f"""INSERT INTO {self.table}(solucion) VALUES('{data['solucion']}')""")
        except Exception as error:
            print("Ocurrió un error insertando los datos: " + str(error))

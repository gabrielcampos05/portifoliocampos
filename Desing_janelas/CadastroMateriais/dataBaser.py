#Gabriel Campos Amaral Ribeiro
#18/07/2023

import sqlite3 as sql

conn=sql.connect('Catalogo.db')

cursor=conn.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS Users(
  Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  Descricao TEXT NOT NULL,  
  Tipo TEXT NOT NULL,  
  Quantidade INTEGER NOT NULL


);
''') 

print('CONECTADO AO BANCO DE DADOS')
import sqlite3

connection = sqlite3.connect('static/db/database.db')

# Base de Datos No.1
with open('static/db/schemaDB_main.sql') as f:
	connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO JUEGOS (juego, enlace, recomendacion) VALUES (?,?,?)",
			("Super Mario 64", "https://es.wikipedia.org/wiki/Super_Mario_64", "1"))
cur.execute("INSERT INTO JUEGOS (juego, enlace, recomendacion) VALUES (?,?,?)",
			("Legend of Zelda Ocarina of Time", "https://es.wikipedia.org/wiki/The_Legend_of_Zelda:_Ocarina_of_Time", "1"))
cur.execute("INSERT INTO JUEGOS (juego, enlace, recomendacion) VALUES (?,?,?)",
			("Downwell", "https://es.wikipedia.org/wiki/Downwell", "0"))

connection.commit()
connection.close()
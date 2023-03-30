import sqlite3

connection = sqlite3.connect('database.db')

# Base de Datos No.1
with open('schemaDB.sql') as f:
	connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
			(1, 'Juan','Bach','95'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
			(2, 'Ludwig','Bethoven','98'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
			(3, 'Federico','Chopin','96'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
			(4, 'Jorge','Handel','95'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
			(5, 'Wolfgang','Mozart','100'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
			(6, 'John','Williams','100'))
cur.execute("INSERT INTO SALON (id, nombre, apellido, calificacion) VALUES (?,?,?,?)",
			(9, 'Esta','es la clave','n7dc86SRVGY&901UpJNTjp1N'))

cur.execute("INSERT INTO JUEGOS (juego, enlace, recomendacion) VALUES (?,?,?)",
			("Super Mario 64", "https://es.wikipedia.org/wiki/Super_Mario_64", "1"))
cur.execute("INSERT INTO JUEGOS (juego, enlace, recomendacion) VALUES (?,?,?)",
			("Legend of Zelda Ocarina of Time", "https://es.wikipedia.org/wiki/The_Legend_of_Zelda:_Ocarina_of_Time", "1"))
cur.execute("INSERT INTO JUEGOS (juego, enlace, recomendacion) VALUES (?,?,?)",
			("Downwell", "https://es.wikipedia.org/wiki/Downwell", "0"))


connection.commit()
connection.close()


#Base de datos No.2
connection = sqlite3.connect('SQLi.db')


with open('schemaSQLi.sql') as f:
	connection.executescript(f.read())

cur = connection.cursor()

for i in range(1, 6):
	i = str(i) 
	cur.execute("INSERT INTO SALON" + i + " (id" + i + ", nombre" + i + ", apellido" + i + ", calificacion" + i + ") VALUES (?,?,?,?)",
				(1, 'Juan','Bach','95'))
	cur.execute("INSERT INTO SALON" + i + " (id" + i + ", nombre" + i + ", apellido" + i + ", calificacion" + i + ") VALUES (?,?,?,?)",
				(2, 'Ludwig','Bethoven','98'))
	cur.execute("INSERT INTO SALON" + i + " (id" + i + ", nombre" + i + ", apellido" + i + ", calificacion" + i + ") VALUES (?,?,?,?)",
				(3, 'Federico','Chopin','96'))
	cur.execute("INSERT INTO SALON" + i + " (id" + i + ", nombre" + i + ", apellido" + i + ", calificacion" + i + ") VALUES (?,?,?,?)",
				(4, 'Jorge','Handel','95'))
	cur.execute("INSERT INTO SALON" + i + " (id" + i + ", nombre" + i + ", apellido" + i + ", calificacion" + i + ") VALUES (?,?,?,?)",
				(5, 'Wolfgang','Mozart','100'))
	cur.execute("INSERT INTO SALON" + i + " (id" + i + ", nombre" + i + ", apellido" + i + ", calificacion" + i + ") VALUES (?,?,?,?)",
				(6, 'John','Williams','100'))

connection.commit()
connection.close()
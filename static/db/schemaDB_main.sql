DROP TABLE IF EXISTS JUEGOS;

CREATE TABLE JUEGOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    juego TEXT NOT NULL,
    enlace TEXT,
    recomendacion INTEGER NOT NULL
);
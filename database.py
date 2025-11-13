import sqlite3


def inicializar_db():
    conexion = sqlite3.connect("leaderboard.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS puntuaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puntos INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()


def guardar_puntuacion(nombre, puntos):
    conexion = sqlite3.connect("leaderboard.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO puntuaciones (nombre, puntos) VALUES (?, ?)", (nombre, puntos))
    conexion.commit()
    conexion.close()


def obtener_top(n=5):
    conexion = sqlite3.connect("leaderboard.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, puntos FROM puntuaciones ORDER BY puntos DESC LIMIT ?", (n,))
    top = cursor.fetchall()
    conexion.close()
    return top


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

def eliminar_datos():
    conexion = sqlite3.connect("leaderboard.db")
    cursor = conexion.cursor()
    cursor.execute("""
        DELETE FROM puntuaciones;
    """)
    conexion.commit()
    conexion.close()

def amigos_puntajes():
    conexion = sqlite3.connect("leaderboard.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO puntuaciones (id, nombre, puntos) 
        VALUES
        (1, 'Cosmo', 5000), (2, 'Nico', 3000), (3, 'Eve', 1500), (4, 'Ramf', 1250), (5, 'Criz', 1000)
    """)
    conexion.commit()
    conexion.close()
    

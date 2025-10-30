import mysql.connector
#from mysql.connector import Error

import pymysql

class ConexConexion:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                user='root',
                host='localhost',
                database='soporte_tecnico',
                password='',  # Asegúrate de que este valor es correcto
                port=3306
            )
            if self.connection:
                print("Conexión exitosa a la base de datos")
        # Cambiamos mysql.connector.Error por pymysql.MySQLError
        except pymysql.MySQLError as e:
            print(f"Error al conectar a MySQL: {e}")
            self.connection = None  # Asignar None si la conexión falla

    def __enter__(self):
        if self.connection:
            self.micursor = self.connection.cursor()  # Crea el cursor aquí
            return self  # Devuelve la instancia de la clase
        else:
            raise RuntimeError("No se pudo establecer la conexión a la base de datos")

    def __exit__(self, exc_type, exc_value, traceback):
        if self.micursor:  # Cierra el cursor si existe
            self.micursor.close()
        if self.connection:  # Cierra la conexión
            self.connection.close()

if __name__ == "__main__":
    with ConexConexion() as db:
        print("✅ Conexión establecida correctamente.")

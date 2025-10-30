import pymysql
from conexion_db import ConexConexion
class UsuarioDB:
#REGISTRO DE USUARIOS
    def crear_usuario(self, idusuario,  nombre, apellido, departamento, correo, tipo, estatu):
        try:
            # Inserta datos en la tabla "usuario"
            sql_insert = "INSERT INTO usuario (idusuario, nombre, apellido, departamento, correo, tipo, estatu) VALUES (%s, %s, %s,%s, %s, %s, %s)"
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_insert, (idusuario, nombre, apellido, departamento, correo, tipo, estatu))
                conexion.connection.commit()
            print("Datos insertados en la tabla 'usuarios'.")
            

            # Limpiar los campos después de la inserción
            

            return True  # Indica que la inserción fue exitosa

        except pymysql.MySQLError as e:
            print("Error al insertar datos en la tabla 'usuario':", e)
            return False  # Indica que hubo un error durante la inserción
        
        
    def buscar_usuario(self, idusuario):
        try:
            sql_select = "SELECT * FROM usuario WHERE idusuario = %s"
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_select, (idusuario,))
                resultado = conexion.micursor.fetchone()
                print(resultado)  # Imprimir el resultado para verificar
                if resultado:
                    return resultado
                else:
                    print(f"No se encontró ningún registro el id {idusuario}")
                    return None
        except pymysql.MySQLError as e:
            print(f"Error al buscar el usuario el id {idusuario}: {e}")
            return None
        
    def actualizar_usuario(self, idusuario, nombre, apellido, departamento, correo, tipo, estatu):
        try:
            sql_update = "UPDATE usuario SET nombre=%s, apellido=%s, departamento=%s, correo=%s, tipo=%s, estatu=%s WHERE idusuario=%s"
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_update, (nombre, apellido, departamento, correo, tipo, estatu, idusuario))
                conexion.connection.commit()

                if conexion.micursor.rowcount == 0:
                    print(f"No se encontró ningún registro con id {idusuario} para actualizar.")
                    return False
                else: 
                    print(f"Usuario con id {idusuario} actualizado correctamente.")
                    return True
        except pymysql.MySQLError as e:
            print(f"Error al actualizar el usuario con id {idusuario}: {e}")
            return False
        
    def eliminar_usuario(self, idusuario):
        try:
            sql_delete = "DELETE FROM usuario WHERE idusuario=%s"
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_delete, (idusuario,))
                conexion.connection.commit()

                if conexion.micursor.rowcount == 0:
                    print(f"No se encontró ningún registro con id {idusuario} para eliminar.")
                    return False
                else:
                    print(f"Usuario con id {idusuario} eliminado correctamente.")
                    return True
        except pymysql.MySQLError as e:
            print(f"Error al eliminar el usuario con id {idusuario}: {e}")
            return False

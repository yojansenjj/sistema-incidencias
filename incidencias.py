import pymysql
from conexion_db import ConexConexion

class incidenciaDB:
    #REGISTRO DE TICKETS
    def crear_incidencia(self, id_incidencias, descripcion, categoria, prioridad, fecha_reporte, fecha_cierre, estado, solicitante_id, tecnico_id):
        try:
            sql_insert = """
                INSERT INTO incidencias (
                    id_incidencias, descripcion, categoria, prioridad, fecha_reporte, fecha_cierre, estado, solicitante_id, tecnico_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_insert, (
                    id_incidencias, descripcion, categoria, prioridad, fecha_reporte, fecha_cierre, estado, solicitante_id, tecnico_id
                ))
                conexion.connection.commit()
            print("✅ Datos insertados correctamente en la tabla 'incidencias'.")
            return True

        except pymysql.MySQLError as e:
            print("❌ Error al insertar datos en la tabla 'incidencias':", e)
            return False


    
    def buscar_incidencia(self, id_incidencias):
        try:
            sql_select = "SELECT * FROM incidencias WHERE id_incidencias = %s"
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_select, (id_incidencias,))
                resultado = conexion.micursor.fetchone()

                if resultado:
                    print(f"✅ Incidencia con id {id_incidencias} encontrada: {resultado}")
                    return resultado
                else:
                    print(f"❌ No se encontró ningún registro con id {id_incidencias}")
                    return None

        except pymysql.MySQLError as e:
            print(f"❌ Error al buscar la incidencia con id {id_incidencias}: {e}")
            return None

    def actualizar_incidencia(self, id_incidencias, descripcion, categoria, prioridad, fecha_reporte, fecha_cierre, estado, solicitante_id, tecnico_id):
        try:
            sql_update = """
                UPDATE incidencias
                SET descrpcion = %s,
                    categoria = %s,
                    prioridad = %s,
                    fecha_reporte = %s,
                    fecha_cierre = %s,
                    estado = %s,
                    solicitante_id = %s,
                    tecnico_id = %s
                WHERE id_incidencias = %s
            """
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_update, (
                    descripcion, categoria, prioridad, fecha_reporte, fecha_cierre, estado, solicitante_id, tecnico_id, id_incidencias
                ))
                conexion.connection.commit()

                if conexion.micursor.rowcount == 0:
                    print(f"⚠️ No se encontró ningún registro con id {id_incidencias} para actualizar.")
                    return False
                else:
                    print(f"✅ Incidencia con id {id_incidencias} actualizada correctamente.")
                    return True
        except pymysql.MySQLError as e:
            print(f"❌ Error al actualizar la incidencia con id {id_incidencias}: {e}")
            return False

        
    def eliminar_incidencia(self, id_incidencias):
        try:
            sql_delete = "DELETE FROM incidencias WHERE id_incidencias=%s"
            with ConexConexion() as conexion:
                conexion.micursor.execute(sql_delete, (id_incidencias,))
                conexion.connection.commit()

                if conexion.micursor.rowcount == 0:
                    print(f"No se encontró ningún registro con id {id_incidencias} para eliminar.")
                    return False
                else:
                    print(f"Incidencia con id {id_incidencias} eliminado correctamente.")
                    return True
        except pymysql.MySQLError as e:
            print(f"Error al eliminar el incidencias con id {id_incidencias}: {e}")
            return False
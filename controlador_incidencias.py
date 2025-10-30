from incidencias import incidenciaDB


class ControladorIncidencias:
    def __init__(self):
        self.modelo = incidenciaDB()

    def registrar_incidencia(self, descripcion, categoria, prioridad, fecha_reporte, fecha_cierre, estado, usuario_id, tecnico_asignado_id):
        """
        Valida los datos y llama al método del modelo para registrar una nueva incidencia.
        """
        if not descripcion or not categoria or not prioridad:
            return False, "Todos los campos obligatorios deben llenarse."

        try:
            self.modelo.crear_incidencia(
                descripcion, categoria, prioridad,
                fecha_reporte, fecha_cierre,
                estado, usuario_id, tecnico_asignado_id
            )
            return True, "✅ Incidencia registrada correctamente."
        except Exception as e:
            return False, f"❌ Error al registrar incidencia: {e}"

    def obtener_todas_incidencias(self):
        """
        Devuelve una lista con todas las incidencias registradas.
        """
        try:
            incidencias = self.modelo.obtener_todas()
            return incidencias
        except Exception as e:
            print("Error al obtener incidencias:", e)
            return []

    def buscar_incidencia(self, id_incidencias):
        """
        Busca una incidencia por su ID.
        """
        try:
            resultado = self.modelo.buscar_incidencia(id_incidencias)
            if resultado:
                return True, resultado
            else:
                return False, "No se encontró ninguna incidencia con ese ID."
        except Exception as e:
            return False, f"Error al buscar incidencia: {e}"

    def actualizar_incidencia(self, id_incidencias, descripcion, categoria, prioridad, fecha_reporte, fecha_cierre, estado, usuario_id, tecnico_asignado_id):
        """
        Actualiza una incidencia existente.
        """
        if not id_incidencias:
            return False, "Debe indicar el ID de la incidencia para actualizar."

        try:
            ok = self.modelo.actualizar_incidencia(
                id_incidencias, descripcion, categoria, prioridad,
                fecha_reporte, fecha_cierre, estado,
                usuario_id, tecnico_asignado_id
            )
            if ok:
                return True, "✅ Incidencia actualizada correctamente."
            else:
                return False, "⚠️ No se encontró la incidencia para actualizar."
        except Exception as e:
            return False, f"❌ Error al actualizar incidencia: {e}"

    def eliminar_incidencia(self, id_incidencias):
        """
        Elimina una incidencia por su ID.
        """
        try:
            ok = self.modelo.eliminar_incidencia(id_incidencias)
            if ok:
                return True, "✅ Incidencia eliminada correctamente."
            else:
                return False, "⚠️ No se encontró la incidencia para eliminar."
        except Exception as e:
            return False, f"❌ Error al eliminar incidencia: {e}"

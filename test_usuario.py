from conexion_db import ConexConexion
from usuarios import UsuarioDB
from datetime import datetime

# Crear una instancia de la clase
ticket_manager = UsuarioDB()

# --- PRUEBA DE INSERCIÓN ---
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
resultado_insert = ticket_manager.crear_usuario(1, "Error de red", "El sistema no conecta", "Alta", "Abierto", fecha, 101)
print("Inserción:", resultado_insert)

# --- PRUEBA DE BÚSQUEDA ---
resultado_busqueda = ticket_manager.buscar_usuario(1)
print("Búsqueda:", resultado_busqueda)

# --- PRUEBA DE ACTUALIZACIÓN ---
resultado_update = ticket_manager.actualizar_usuario(1, "Error de red corregido", "Ya se solucionó", "Media", "Cerrado", fecha, 101)
print("Actualización:", resultado_update)

# --- PRUEBA DE ELIMINACIÓN ---
resultado_delete = ticket_manager.eliminar_usuario(1)
print("Eliminación:", resultado_delete)

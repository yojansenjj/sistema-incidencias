import tkinter as tk
from tkinter import ttk, messagebox
from incidencias import incidenciaDB
from conexion_db import ConexConexion
from controlador_incidencias import ControladorIncidencias
from datetime import datetime

# ==============================
# Ventana principal
# ==============================
class AppSoporteTecnico(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Incidencias - Soporte Técnico")
        self.geometry("1000x600")
        self.configure(bg="#f5f6f7")

        # Estilo general
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=[10, 5])
        style.configure("TNotebook", background="#ffffff")

        # Crear las pestañas principales
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Agregar pestañas
        self.tab_usuarios = ttk.Frame(self.notebook)
        self.tab_incidencias = ttk.Frame(self.notebook)
        self.tab_reportes = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_usuarios, text="Usuarios")
        self.notebook.add(self.tab_incidencias, text="Incidencias")
        self.notebook.add(self.tab_reportes, text="Reportes")

        # Inicializar contenidos
        self.interfaz_usuarios()
        self.interfaz_incidencias()
        self.interfaz_reportes()

    # ==============================
    # Pestaña 1: Usuarios
    # ==============================
    def interfaz_usuarios(self):
        ttk.Label(self.tab_usuarios, text="Gestión de Usuarios", font=("Segoe UI", 12, "bold")).pack(pady=10)

        frm = ttk.Frame(self.tab_usuarios, padding=10)
        frm.pack(fill="x")

        ttk.Label(frm, text="ID Usuario:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(frm).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Nombre:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(frm).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Tipo (Técnico/Solicitante):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Combobox(frm, values=["Técnico", "Solicitante"]).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frm, text="Registrar Usuario", style="Accent.TButton").grid(row=3, column=1, pady=10, sticky="e")

    # ==============================
    # Pestaña 2: Incidencias
    # ==============================
    def interfaz_incidencias(self):
        ttk.Label(self.tab_incidencias, text="Gestión de Incidencias", font=("Segoe UI", 12, "bold")).pack(pady=10)

        frm = ttk.Frame(self.tab_incidencias, padding=10)
        frm.pack(fill="x")

        campos = [
            ("ID Incidencia:", 0),
            ("Descripción:", 1),
            ("Categoría:", 2),
            ("Prioridad:", 3),
            ("Fecha Reporte:", 4),
            ("Fecha Cierre:", 5),
            ("Estado:", 6)
        ]

        for texto, fila in campos:
            ttk.Label(frm, text=texto).grid(row=fila, column=0, sticky="e", padx=5, pady=5)
            ttk.Entry(frm).grid(row=fila, column=1, padx=5, pady=5)

        ttk.Button(frm, text="Registrar Incidencia").grid(row=8, column=1, pady=10, sticky="e")

        # Tabla para mostrar incidencias
        ttk.Label(self.tab_incidencias, text="Listado de Incidencias").pack(pady=10)
        columnas = ("ID", "Descripción", "Categoría", "Prioridad", "Estado", "Fecha Reporte", "Fecha Cierre")

        tabla = ttk.Treeview(self.tab_incidencias, columns=columnas, show="headings", height=10)
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=120, anchor="center")
        tabla.pack(fill="both", expand=True, padx=10, pady=10)

    # ==============================
    # Pestaña 3: Reportes
    # ==============================
    def interfaz_reportes(self):
        ttk.Label(self.tab_reportes, text="Generación de Reportes", font=("Segoe UI", 12, "bold")).pack(pady=20)
        ttk.Button(self.tab_reportes, text="Generar Reporte PDF").pack(pady=10)
        ttk.Button(self.tab_reportes, text="Exportar a Excel").pack(pady=10)

# ==============================
# Ejecutar la aplicación
# ==============================
if __name__ == "__main__":
    app = AppSoporteTecnico()
    app.mainloop()

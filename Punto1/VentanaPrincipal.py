from Notas import Notas
import tkinter as tk
from tkinter import ttk, messagebox

class VentanaPrincipal(tk.Tk): # Hereda directamente de tk.Tk
                                # como corregimos en el paso anterior

    def __init__(self):
        """
        Constructor de la clase VentanaPrincipal.
        Crea la interfaz gráfica de usuario.
        """
        super().__init__() # Llama al constructor de tk.Tk
        self.title("Calculadora de Notas")
        self.geometry("300x400")
        self.resizable(False, False)

        # Instancia de la clase Notas para realizar los cálculos
        self.notas = Notas()

        self._inicio() # Llama al método que crea los componentes gráficos

    def _inicio(self):
        """
        Método que crea la ventana con sus diferentes componentes gráficos.
        """
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10))
        style.configure("TEntry", font=("Arial", 10))

        # Etiquetas y campos de texto para las notas
        ttk.Label(self, text="Nota 1:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.campoNota1 = ttk.Entry(self, width=15)
        self.campoNota1.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self, text="Nota 2:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.campoNota2 = ttk.Entry(self, width=15)
        self.campoNota2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self, text="Nota 3:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.campoNota3 = ttk.Entry(self, width=15)
        self.campoNota3.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self, text="Nota 4:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.campoNota4 = ttk.Entry(self, width=15)
        self.campoNota4.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self, text="Nota 5:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.campoNota5 = ttk.Entry(self, width=15)
        self.campoNota5.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        # Botones para realizar cálculos y para borrar las notas
        # AHORA: Asignamos métodos específicos a cada botón
        self.calcular = ttk.Button(self, text="Calcular", command=self._on_calcular_click)
        self.calcular.grid(row=5, column=0, padx=10, pady=20, sticky="ew")

        self.limpiar = ttk.Button(self, text="Limpiar", command=self._on_limpiar_click)
        self.limpiar.grid(row=5, column=1, padx=10, pady=20, sticky="ew")

        # Etiquetas de resultados
        self.promedio_label = ttk.Label(self, text="Promedio = ")
        self.promedio_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.desviacion_label = ttk.Label(self, text="Desviación estándar = ")
        self.desviacion_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.mayor_label = ttk.Label(self, text="Valor mayor = ")
        self.mayor_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.menor_label = ttk.Label(self, text="Valor menor = ")
        self.menor_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    # NUEVO: Método específico para el botón "Calcular"
    def _on_calcular_click(self):
        """
        Maneja el evento de click del botón 'Calcular'.
        """
        notas_str = [
            self.campoNota1.get(),
            self.campoNota2.get(),
            self.campoNota3.get(),
            self.campoNota4.get(),
            self.campoNota5.get()
        ]
        
        try:
            for i, nota_str in enumerate(notas_str):
                nota = float(nota_str)
                if not (0 <= nota <= 5):
                    messagebox.showerror("Error de Nota", "Todas las notas deben estar entre 0 y 5.")
                    return
                self.notas.listaNotas[i] = nota # Asigna la nota validada a la instancia de Notas
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese valores numéricos válidos para las notas.")
            return

        # Realiza los cálculos usando la instancia de Notas
        promedio = self.notas.calcularPromedio()
        desviacion = self.notas.calcularDesviacion()
        mayor_valor = self.notas.calcularMayor()
        menor_valor = self.notas.calcularMenor()

        # Muestra los resultados formateados
        self.promedio_label.config(text=f"Promedio = {promedio:.2f}")
        self.desviacion_label.config(text=f"Desviación estándar = {desviacion:.2f}")
        self.mayor_label.config(text=f"Valor mayor = {mayor_valor:.1f}")
        self.menor_label.config(text=f"Valor menor = {menor_valor:.1f}")

    # NUEVO: Método específico para el botón "Limpiar"
    def _on_limpiar_click(self):
        """
        Maneja el evento de click del botón 'Limpiar'.
        """
        # Se dejan en blanco los campos de notas
        self.campoNota1.delete(0, tk.END)
        self.campoNota2.delete(0, tk.END)
        self.campoNota3.delete(0, tk.END)
        self.campoNota4.delete(0, tk.END)
        self.campoNota5.delete(0, tk.END)

        # Limpiar también las etiquetas de resultado
        self.promedio_label.config(text="Promedio = ")
        self.desviacion_label.config(text="Desviación estándar = ")
        self.mayor_label.config(text="Valor mayor = ")
        self.menor_label.config(text="Valor menor = ")
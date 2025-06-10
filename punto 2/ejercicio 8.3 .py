import math
import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------------------------
# CLASES DEL MODELO (FIGURAS GEOMÉTRICAS)
# ---------------------------------------------------------------------------

class FiguraGeometrica:
    """
    Esta clase denominada FiguraGeométrica modela una figura
    geométrica que cuenta con un volumen y una superficie.
    Es la clase padre para las figuras específicas.
    """
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

class Cilindro(FiguraGeometrica):
    """
    Esta clase denominada Cilindro es una subclase de FiguraGeométrica
    que cuenta con un radio y una altura.
    """
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio ** 2)

    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_bases = 2 * math.pi * (self.radio ** 2)
        return area_lateral + area_bases

class Esfera(FiguraGeometrica):
    """
    Esta clase denominada Esfera es una subclase de FiguraGeométrica
    que cuenta con un radio.
    """
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        return 4 * math.pi * (self.radio ** 2)

class Piramide(FiguraGeometrica):
    """
    Esta clase denominada Pirámide es una subclase de FiguraGeométrica
    que cuenta con una base, una altura y un apotema.
    """
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return ((self.base ** 2) * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral

# ---------------------------------------------------------------------------
# CLASES DE LA VISTA (VENTANAS DE LA GUI CON TKINTER)
# ---------------------------------------------------------------------------

class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)  # CORRECCIÓN AQUÍ
        self.inicializar_componentes()

    def inicializar_componentes(self):
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=135)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=80, width=135)

        self.label_volumen = tk.Label(self, text="Volumen (cm³):")
        self.label_volumen.place(x=20, y=110)
        self.label_superficie = tk.Label(self, text="Superficie (cm²):")
        self.label_superficie.place(x=20, y=140)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)
            
            self.label_volumen.config(text=f"Volumen (cm³): {cilindro.volumen:.2f}")
            self.label_superficie.config(text=f"Superficie (cm²): {cilindro.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.", parent=self)

class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)  # CORRECCIÓN AQUÍ
        self.inicializar_componentes()

    def inicializar_componentes(self):
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=100, y=50, width=135)

        self.label_volumen = tk.Label(self, text="Volumen (cm³):")
        self.label_volumen.place(x=20, y=90)
        self.label_superficie = tk.Label(self, text="Superficie (cm²):")
        self.label_superficie.place(x=20, y=120)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            
            self.label_volumen.config(text=f"Volumen (cm³): {esfera.volumen:.2f}")
            self.label_superficie.config(text=f"Superficie (cm²): {esfera.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.", parent=self)

class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)  # CORRECCIÓN AQUÍ
        self.inicializar_componentes()

    def inicializar_componentes(self):
        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50, width=135)

        tk.Label(self, text="Apotema (cms):").place(x=20, y=80)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=80, width=135)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=120, y=110, width=135)

        self.label_volumen = tk.Label(self, text="Volumen (cm³):")
        self.label_volumen.place(x=20, y=140)
        self.label_superficie = tk.Label(self, text="Superficie (cm²):")
        self.label_superficie.place(x=20, y=170)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            piramide = Piramide(base, altura, apotema)
            
            self.label_volumen.config(text=f"Volumen (cm³): {piramide.volumen:.2f}")
            self.label_superficie.config(text=f"Superficie (cm²): {piramide.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.", parent=self)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)  # CORRECCIÓN AQUÍ
        self.inicializar_componentes()

    def inicializar_componentes(self):
        tk.Button(self, text="Cilindro", command=self.mostrar_ventana_cilindro).place(x=20, y=50, width=80)
        tk.Button(self, text="Esfera", command=self.mostrar_ventana_esfera).place(x=125, y=50, width=80)
        tk.Button(self, text="Pirámide", command=self.mostrar_ventana_piramide).place(x=225, y=50, width=100)

    def mostrar_ventana_cilindro(self):
        VentanaCilindro(self)

    def mostrar_ventana_esfera(self):
        VentanaEsfera(self)

    def mostrar_ventana_piramide(self):
        VentanaPiramide(self)

# ---------------------------------------------------------------------------
# PUNTO DE ENTRADA PRINCIPAL DE LA APLICACIÓN
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
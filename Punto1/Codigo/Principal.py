import tkinter as tk
from VentanaPrincipal import VentanaPrincipal

class Principal:
    @staticmethod
    def main():
        mi_ventana = VentanaPrincipal()
        mi_ventana.mainloop()

if __name__ == "__main__":
    Principal.main()

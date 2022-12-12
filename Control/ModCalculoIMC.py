from tkinter import messagebox

from Entity.DAO import CursoCRUD


def isNumeric(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


class CalculoIMC:
    def __init__(self):
        self.imc = 0
        self.rangeIMC = ''

    def CalcularIMC(self, height, weight):
        if isNumeric(height) and isNumeric(weight):
            h = float(height)
            w = float(weight)
            if h > 1 and w > 10:
                self.imc = round(w / (h ** 2), 2)
                if self.imc > 10:
                    if self.imc < 18.5:
                        self.rangeIMC = 'Bajo peso'
                    elif 18.5 <= self.imc <= 24.9:
                        self.rangeIMC = 'Saludable'
                    elif 25 <= self.imc <= 29.9:
                        self.rangeIMC = 'Sobrepeso'
                    else:
                        self.rangeIMC = 'Obesidad'
                    return True
                else:
                    messagebox.showerror("Error", "Peso o altura inválidos")
                    return False
            else:
                messagebox.showerror("Error", "Peso o altura inválidos")
                return False
        else:
            messagebox.showerror("Error", "Ingrese altura y peso válidos (Números)")
            return False

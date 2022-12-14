from tkinter import Tk

from Boundary.ModInterfaceCalculoIMC import FrameCalculoIMC


root = Tk()
root.title("Sistema IMC - Profesor")

root.eval('tk::PlaceWindow . center')
root.resizable(False, False)

app = FrameCalculoIMC(root)
app.mainloop()

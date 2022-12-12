from tkinter import Tk

from Boundary.ModInterfaceAdmin import FrameReportAdmin

root2 = Tk()
root2.title('Sistema IMC - Administrativo')

root2.eval('tk::PlaceWindow . center')
root2.resizable(False, False)

app2 = FrameReportAdmin(root2)
app2.mainloop()

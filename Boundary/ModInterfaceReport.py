from tkinter import *
from tkinter import font

from Entity.DAO import EstudianteCRUD, CursoCRUD, RegistroCRUD
from Control.ModAdminReport import Reporte


class TopLevelReport(Toplevel):
    def __init__(self, master=None, rut=None, id_grade=None):
        super().__init__(master, width=500, height=350, padx=10, pady=5, bg='#113f67')
        self.master = master
        self.rut = rut
        self.id_grade = id_grade

        self.objReg = Reporte(self.rut, self.id_grade)

        self.info_imc = self.objReg.calcular_prom_imc() #Collection
        self.grade = CursoCRUD.mostrar_x_id(id_grade)[1].capitalize()
        self.section = CursoCRUD.mostrar_x_id(id_grade)[2].capitalize()
        self.cant_alumnos = EstudianteCRUD.mostrar_cant_alumnos(self.id_grade)[0]

        self.name = EstudianteCRUD.mostrar_x_rut(self.rut)[1] + " " + EstudianteCRUD.mostrar_x_rut(self.rut)[2]
        self.imc = RegistroCRUD.mostrar_ultimo_registro(rut)[1]
        self.rango_imc = RegistroCRUD.mostrar_ultimo_registro(rut)[2]
        self.age = self.objReg.calcular_edad()
        self.genre = self.objReg.get_genre()

        self.setFrameFont()
        self.widgets()

    def setFrameFont(self):
        self.defaultFont = font.nametofont("TkDefaultFont", self.master)
        self.defaultFont.config(family="Segoe UI",
                                size=9,
                                slant=font.ITALIC)

    def widgets(self):
        Label(self, text='Reporte estudiante \n comparado promedio del curso', bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 12, font.BOLD)).grid(row=0, column=0)
        self.frameReport = LabelFrame(self, text='Reporte Estudiante/Curso', bg='#113f67', fg='#a2a8d3', padx=15, pady=10)
        self.frameReport.grid(row=1, column=0)

        Label(self.frameReport, text=self.name, bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 10, font.BOLD)).grid(row=0, column=0, sticky='w', columnspan=4)

        Label(self.frameReport, text='Edad:', bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 9, font.NORMAL)).grid(row=1, column=0, sticky='e')
        Label(self.frameReport, text=self.age, bg='#113f67', fg='#a2a8d3').grid(row=1, column=1, sticky='w')

        Label(self.frameReport, text='Género:', bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 9, font.NORMAL)).grid(row=2, column=0, sticky='e')
        Label(self.frameReport, text=self.genre, bg='#113f67', fg='#a2a8d3').grid(row=2, column=1, sticky='w')

        Label(self.frameReport, text='IMC: ', bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 9, font.NORMAL)).grid(row=2, column=2, sticky='e')
        Label(self.frameReport, text=self.imc, bg='#113f67', fg='#a2a8d3').grid(row=2, column=3, sticky='w')

        Label(self.frameReport, text='Rango IMC: ', bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 9, font.NORMAL)).grid(row=1, column=2, sticky='e')
        Label(self.frameReport, text=self.rango_imc, bg='#113f67', fg='#a2a8d3').grid(row=1, column=3, sticky='e')

        Label(self.frameReport, text=self.grade + " " + self.section, bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 10, font.BOLD)).grid(row=4, column=0, sticky='w', columnspan=4)

        Label(self.frameReport, text='IMC:', bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 9, font.NORMAL)).grid(row=6, column=0, sticky='e')
        Label(self.frameReport, text=self.info_imc[0], bg='#113f67', fg='#a2a8d3').grid(row=6, column=1, sticky='w')

        Label(self.frameReport, text='Rango IMC:', bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 9)).grid(row=5, column=0, sticky='e')
        Label(self.frameReport, text=self.info_imc[1], bg='#113f67', fg='#a2a8d3').grid(row=5, column=1, sticky='w')

        Label(self.frameReport, text='Alumnos:', bg='#113f67', fg='#a2a8d3',
              font=("Segoe UI", 9, font.NORMAL)).grid(row=5, column=2, sticky='e')
        Label(self.frameReport, text=self.cant_alumnos, bg='#113f67', fg='#a2a8d3').grid(row=5, column=3, sticky='w')


from tkinter import *
from tkinter import font, messagebox
from tkinter.ttk import Combobox

from Control import Others
from Entity.DAO import EstudianteCRUD
from Boundary.ModInterfaceReport import TopLevelReport


class FrameReportAdmin(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=500, height=500, bg='#113f67', padx=10, pady=10)
        self.master = master
        self.pack()
        self.setFrameFont()
        self.widgets()

    def setFrameFont(self):
        self.defaultFont = font.nametofont("TkDefaultFont", self.master)
        self.defaultFont.config(family="Segoe UI",
                                size=9,
                                weight=font.NORMAL)

    def on_combobox_select(self, event): #Show students in grades
        self.boxNombre.set("")

        self.id_grade = (self.boxCurso.get()).split()[0]

        self.boxNombre.config(
            values=Others.datosEstudiantesCB(
                (EstudianteCRUD.mostrar_x_index(self.id_grade))))

    def selectedStudent(self, event): #Asign a new atribute for the frame that contains the student's name
        self.studentSelected = (self.boxNombre.get()).split()[0]

    def generateReport(self):
        if len(self.boxCurso.get()) == 0 and len(self.boxNombre.get()) == 0:
            messagebox.showerror(title='Error selección', message='Seleccione un Estudiante para emitir reporte')
        elif len(self.boxReport.get()) == 0:
            messagebox.showerror(title='Error selección', message='Seleccione un tipo de reporte a emitir')
        elif self.boxReport.get() == 'Comparado con promedio del curso':
            self.report_wind = TopLevelReport(self, self.studentSelected, self.id_grade)

    def widgets(self):
        Label(self, text='Emitir reporte de estudiante', fg='#a2a8d3', bg='#113f67',
              font=("Segoe UI", 12, font.BOLD)).grid(row=0, column=0, columnspan=10, pady=5, padx=5)

        self.main_frame = LabelFrame(self, text='Selección de emisión', fg='#a2a8d3', bg='#113f67', pady=5, padx=5)
        self.main_frame.grid(row=1, column=0)

        Label(self.main_frame, text='Seleccionar curso: ', fg='#a2a8d3', bg='#113f67').grid(row=0, column=0, sticky='e')
        self.boxCurso = Combobox(self.main_frame, width=20, state='readonly',
                 values=Others.datosCursoCB())
        self.boxCurso.grid(row=0, column=1, sticky='w', pady=5)
        self.boxCurso.bind("<<ComboboxSelected>>", self.on_combobox_select)

        Label(self.main_frame, text='Seleccionar estudiante: ', fg='#a2a8d3', bg='#113f67').grid(row=1, column=0)
        self.boxNombre = Combobox(self.main_frame, width=38, state='readonly')
        self.boxNombre.grid(row=1, column=1, pady=5, sticky='w')
        self.boxNombre.bind('<<ComboboxSelected>>', self.selectedStudent)

        Label(self.main_frame, text='Seleccionar reporte: ', fg='#a2a8d3', bg='#113f67').grid(row=2, column=0, sticky='e')
        self.boxReport = Combobox(self.main_frame, width=38, state='readonly',
                                  values=['Evolución de estudiante', 'Comparado con promedio del curso',
                                          'Comparado con compañeros misma edad',
                                          'Comparado con mismo sexo (Curso)'])
        self.boxReport.grid(row=2, column=1, sticky='w', pady=5)

        Button(self.main_frame, text='Generar reporte', width=15, bg='#113f67', fg='#a2a8d3',
               command=self.generateReport).grid(row=5, column=1, pady=15, sticky='w', columnspan=2)

        Button(self.main_frame, text='Volver', width=10, bg='#113f67', fg='#a2a8d3',
               command='').grid(row=5, column=0, sticky='w', padx=15, pady=10)
        Button(self.main_frame, text='Salir', width=10, bg='#113f67', fg='#a2a8d3',
               command=self.master.destroy).grid(row=5, column=1, sticky='e', padx=15, pady=5)

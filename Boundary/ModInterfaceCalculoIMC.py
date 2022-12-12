from tkinter import messagebox, font
from datetime import *
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox
from Entity.DAO import EstudianteCRUD
from Entity.DTO.RegistroDTO import RegistroIMC
from Entity.DAO import RegistroCRUD
from Control.ModCalculoIMC import isNumeric
from Control import Others

from Control.ModCalculoIMC import CalculoIMC


class FrameCalculoIMC(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=500, height=500, bg='#113f67', padx=10, pady=10)  # config
        self.imc = None
        self.rango_imc = None
        self.master = master
        self.pack()
        self.objCalculoIMC = CalculoIMC()
        self.setFrameFont()
        self.widgets()

    def fnCalcular(self):
        if self.fieldPeso.get() != '' or self.fieldAltura.get() != '':
            w = self.fieldPeso.get()
            h = self.fieldAltura.get()
            if self.objCalculoIMC.CalcularIMC(h, w):
                self.imc = self.objCalculoIMC.imc
                self.rango_imc = self.objCalculoIMC.rangeIMC

                self.fieldRangoIMC.config(state='normal')
                self.fieldIMC.config(state='normal')

                self.fieldIMC.delete(0, 'end')
                self.fieldRangoIMC.delete(0, 'end')
                self.fieldIMC.insert(0, self.imc)

                self.fieldRangoIMC.insert(0, self.rango_imc)
                self.fieldPeso.config(state='readonly')
                self.fieldAltura.config(state='readonly')
                self.fieldRangoIMC.config(state='readonly')
                self.fieldIMC.config(state='readonly')
        else:
            messagebox.showerror("Error", "Ingrese altura y peso")

    def fnRegistrar(self):
        if len(self.fieldIMC.get()) != 0:
            imc = float(self.fieldIMC.get())
            if len(self.boxCurso.get()) != 0 and len(self.boxNombre.get()) != 0 and imc > 0:
                rango_imc = self.objCalculoIMC.rangeIMC
                rut_estudiante = self.boxNombre.get().split()[0]
                self.registro_imc = RegistroIMC(imc, rango_imc, "{}-{}-{}"
                                                .format(datetime.now().year,
                                                        datetime.now().month,
                                                        datetime.now().day), rut_estudiante)
                RegistroCRUD.insert(self.registro_imc)
                self.fnLimpiar()

            else:
                messagebox.showerror(title="Error", message="Faltan datos para registrar en el sistema")
        else:
            messagebox.showerror(title="Error", message="Faltan datos para registrar en el sistema")

    def fnLimpiar(self):
        self.fieldPeso.config(state='normal')
        self.fieldAltura.config(state='normal')
        self.fieldRangoIMC.config(state='normal')
        self.fieldIMC.config(state='normal')

        self.fieldPeso.delete(0, 'end')
        self.fieldAltura.delete(0, 'end')
        self.fieldIMC.delete(0, 'end')
        self.fieldRangoIMC.delete(0, 'end')
        self.boxNombre.set('')
        self.boxCurso.set('')
        self.boxNombre.config(values=[''])

        self.fieldPeso.config(state='readonly')
        self.fieldAltura.config(state='readonly')
        self.fieldRangoIMC.config(state='readonly')
        self.fieldIMC.config(state='readonly')

    def on_combobox_select(self, event):
        self.boxNombre.set("")

        index = (self.boxCurso.get()).split()[0]

        self.boxNombre.config(
            values=Others.datosEstudiantesCB(
                (EstudianteCRUD.mostrar_x_index(index))))

    def unlock_imc_section(self, event):
        self.fieldPeso.config(state='normal')
        self.fieldAltura.config(state='normal')

    def setFrameFont(self):
        self.defaultFont = font.nametofont("TkDefaultFont", self.master)
        self.defaultFont.config(family="Segoe UI",
                                size=10,
                                weight=font.NORMAL)

    def widgets(self):

        self.lblTittle = Label(self, text='Sistema IMC', fg='#a2a8d3', bg='#113f67')
        self.lblTittle.grid(row=0, column=0, columnspan=10, pady=5)

        self.mainFrame = LabelFrame(self, text='Registro alumno', bg='#113f67', fg='#a2a8d3', padx=5, pady=5)
        self.mainFrame.grid(row=1, column=0, sticky='w')

        Label(self.mainFrame, text='Curso: ', bg='#113f67', pady=5, padx=5, fg='#a2a8d3').grid(row=0, column=0,
                                                                                               sticky='w')
        self.boxCurso = Combobox(self.mainFrame, width=20,
                                 values=Others.datosCursoCB(), state='readonly')
        self.boxCurso.grid(row=0, column=1, sticky='w')
        self.boxCurso.bind("<<ComboboxSelected>>", self.on_combobox_select)

        Button(self.mainFrame, text='Limpiar', width=8, bg='#113f67', fg='#a2a8d3',
               command=self.fnLimpiar).grid(row=0, column=1, sticky='e', padx=40, pady=10)

        Label(self.mainFrame, text='Nombre: ', bg='#113f67', fg='#a2a8d3').grid(row=1, column=0, sticky='w')
        self.boxNombre = Combobox(self.mainFrame, width=47, state='readonly')
        self.boxNombre.grid(row=1, column=1, sticky='w')
        self.boxNombre.bind('<<ComboboxSelected>>', self.unlock_imc_section)

        self.imcFrame = LabelFrame(self, text='Calculo IMC', bg='#113f67', fg='#a2a8d3', padx=5, pady=5)
        self.imcFrame.grid(row=2, column=0, pady=5)

        Label(self.imcFrame, text='Peso: ', bg='#113f67', fg='#a2a8d3').grid(row=0, column=0)
        self.fieldPeso = Entry(self.imcFrame, width=15, state='readonly')
        self.fieldPeso.grid(row=0, column=1, sticky='w')
        Label(self.imcFrame, text='[Kg]', bg='#113f67', fg='#a2a8d3').grid(row=0, column=2, padx=5, sticky='w')

        Label(self.imcFrame, text='Altura: ', bg='#113f67', fg='#a2a8d3').grid(row=1, column=0)
        self.fieldAltura = Entry(self.imcFrame, width=15, state='readonly')
        self.fieldAltura.grid(row=1, column=1, sticky='w', pady=5)
        Label(self.imcFrame, text='[m]', bg='#113f67', fg='#a2a8d3').grid(row=1, column=2, padx=5, sticky='w')

        Label(self.imcFrame, text='IMC: ', bg='#113f67', fg='#a2a8d3').grid(row=0, column=4, sticky='e')
        self.fieldIMC = Entry(self.imcFrame, width=5, state='readonly')
        self.fieldIMC.grid(row=0, column=5, sticky='w')

        Label(self.imcFrame, text='Rango IMC: ', bg='#113f67', fg='#a2a8d3').grid(row=1, column=4)
        self.fieldRangoIMC = Entry(self.imcFrame, width=15, state='readonly')
        self.fieldRangoIMC.grid(row=1, column=5, pady=10)

        Button(self.imcFrame, text='Volver', width=8, bg='#113f67', fg='#a2a8d3').grid(row=3, column=0, pady=5,
                                                                                       sticky='we')

        Button(self.imcFrame, text='Registrar', width=8, bg='#113f67', fg='#a2a8d3',
               command=self.fnRegistrar).grid(row=3, column=1, pady=5, sticky='e')

        Button(self.imcFrame, text='Calcular', width=8, bg='#113f67', fg='#a2a8d3',
               command=self.fnCalcular).grid(row=3, column=3, pady=5, sticky='w', columnspan=2)

        Button(self.imcFrame, text='Salir', width=8, bg='#113f67', fg='#a2a8d3',
               command=self.master.destroy).grid(row=3, column=4, pady=10, sticky='e', columnspan=4)

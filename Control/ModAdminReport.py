from datetime import datetime

from Entity.DAO import EstudianteCRUD, RegistroCRUD


class Reporte:
    def __init__(self, rut, id_curso):
        self.age = 0
        self.rut = rut
        self.id_curso = id_curso
        self.ano_nac = (str(EstudianteCRUD.mostrar_x_rut(rut)[3])).split("-")[0]
        self.genre = str(EstudianteCRUD.mostrar_x_rut(rut)[4]).lower()

    def calcular_edad(self):
        ano_actual = datetime.today().year
        self.age = int(ano_actual) - int(self.ano_nac)
        return self.age

    def calcular_prom_imc(self):
        #collections
        std_grade = EstudianteCRUD.mostrar_x_index(self.id_curso)
        sum_imc = 0
        total_registros = 0
        for std in std_grade:
            registers = RegistroCRUD.mostrar_ultimo_registro(std[0]) #Collection
            if registers is not None:
                total_registros += 1
                sum_imc += float(registers[1])

        prom_imc = round(sum_imc/total_registros, 2)
        range_imc = ''

        if prom_imc > 10:
            if prom_imc < 18.5:
                range_imc = 'Bajo peso'
            elif 18.5 <= prom_imc <= 24.9:
                range_imc = 'Saludable'
            elif 25 <= prom_imc <= 29.9:
                range_imc = 'Sobrepeso'
            else:
                range_imc = 'Obesidad'

        return [prom_imc, range_imc]

    def get_genre(self):
        if self.genre == 'f':
            return 'Femenino'
        elif self.genre == 'm':
            return 'Masculino'


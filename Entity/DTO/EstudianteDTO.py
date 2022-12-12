class Estudiante:
    def __init__(self, rut, name, last_name, fec_nac, genre, registro_imc, grade):
        self.rut = rut
        self.name = name
        self.last_name = last_name
        self.fec_nac = fec_nac
        self.genre = genre
        self.registro_imc = registro_imc
        self.curso = grade

        self.registros = []

    def addRegister(self):
        pass
from Entity.DAO import CursoCRUD


def datosCursoCB():
    datos = CursoCRUD.mostrar_todo()
    new_datos = []
    for i in range(len(datos)):
        new_datos.append(str(datos[i][0]) + ' - ' + datos[i][1].capitalize() + ' ' + datos[i][2].capitalize())
    return new_datos


def datosEstudiantesCB(datos):
    new_datos = []
    for i in range(len(datos)):
        new_datos.append(str(datos[i][0]) + ' - ' + datos[i][1] + ' ' + datos[i][2])
    return new_datos

from Entity.DTO.Conexion import Connection

host = 'localhost'
port = 3307
user = 'root'
password = ''
db = 'sistema_imc'

def insert(registro):
    try:
        con = Connection(host, port, user, password, db)
        query = "INSERT INTO `registro_imc` (`id_registro`, `imc`, `rango_imc`, `fecha`, `rut_estudiante`) VALUES " \
                "(NULL, '{}', '{}', '{}', '{}');".format(registro.imc, registro.rango_imc, registro.fecha, registro.rut)
        con.ex_query(query)
        con.commit()
        con.disconnect()
    except Exception as e:
        print(e)

def mostrar_ultimo_registro(rut):
    try:
        con = Connection(host, port, user, password, db)
        query = "SELECT * FROM registro_imc WHERE rut_estudiante = '{}' AND fecha = (SELECT MAX(fecha) from registro_imc)".format(rut)
        cursor = con.ex_query(query)
        datos = cursor.fetchone()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def mostrar_all_registros(rut):
    try:
        con = Connection(host, port, user, password, db)
        query = "SELECT * FROM registro_imc WHERE rut_estudiante = '{}' AND fecha = (SELECT MAX(fecha) from registro_imc)".format(rut)
        cursor = con.ex_query(query)
        datos = cursor.fetchmany()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

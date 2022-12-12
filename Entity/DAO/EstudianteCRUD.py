from Entity.DTO.Conexion import Connection

host = 'localhost'
port = 3307
user = 'root'
password = ''
db = 'sistema_imc'

def modify(est):
    try:
        con = Connection(host, port, user, password, db)
        query = ''
        con.ex_query(query)
        con.commit()
        con.disconnect()
    except Exception as e:
        print(e)

def mostrar_todo():
    try:
        con = Connection(host, port, user, password, db)
        query = "select * from estudiantes"
        cursor = con.ex_query(query)
        datos = cursor.fetchall()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def mostrar_x_index(i):
    try:
        con = Connection(host, port, user, password, db)
        query = "select * from estudiantes where id_curso={}".format(i)
        cursor = con.ex_query(query)
        datos = cursor.fetchall()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def mostrar_x_rut(rut):
    try:
        con = Connection(host, port, user, password, db)
        query = "select * from estudiantes where rut='{}'".format(rut)
        cursor = con.ex_query(query)
        datos = cursor.fetchone()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def mostrar_cant_alumnos(id_curso):
    try:
        con = Connection(host, port, user, password, db)
        query = "SELECT COUNT(rut) FROM estudiantes WHERE id_curso={};".format(id_curso)
        cursor = con.ex_query(query)
        datos = cursor.fetchone()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

from Entity.DTO.Conexion import Connection

host = 'localhost'
port = 3307
user = 'root'
password = ''
db = 'sistema_imc'


def insert(curso):
    try:
        con = Connection(host, port, user, password, db)
        query = "INSERT INTO `cursos` (`id_curso`, `nivel`, `seccion`) VALUES (NULL, '{}', '{}');" \
            .format(curso.nivel, curso.seccion)
        con.ex_query(query)
        con.commit()
        con.disconnect()
    except Exception as e:
        print(e)


def consulta_por_nivel(nivel):  # Primero medio, primero basico, etc
    try:
        con = Connection(host, port, user, password, db)
        query = "select * from cursos where nivel={}".format(nivel)
        cursor = con.ex_query(query)
        datos = cursor.fetchone()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)


def consulta_por_seccion(seccion):
    try:
        con = Connection(host, user, password, db)
        query = "select * from cursos where seccion={}".format(seccion)
        cursor = con.ex_query(query)
        datos = cursor.fetchone()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def mostrar_todo():
    try:
        con = Connection(host, port, user, password, db)
        query = "select * from cursos"
        cursor = con.ex_query(query)
        datos = cursor.fetchall()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)

def mostrar_x_id(id):
    try:
        con = Connection(host, port, user, password, db)
        query = "select * from cursos where id_cursos='{}'".format(id)
        cursor = con.ex_query(query)
        datos = cursor.fetchone()
        con.disconnect()
        return datos
    except Exception as e:
        con.rollback()
        print(e)
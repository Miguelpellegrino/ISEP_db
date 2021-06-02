import sqlite3
from sqlite3 import Error
from os import system 

database = "data.db"
lead = 'usuario'
def create_db(db):
    create = None
    try:
        create = sqlite3.connect(db)
        cursor = create.cursor()
        cursor.execute('''
            CREATE TABLE %s
            (id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            email text NOT NULL,
            tel text NOT NULL)''' % lead)
        create.commit()
        return create
    except Error:
        pass
        #print(Error)
    finally:
        if create:
            create.close()

def connect_db(database = database):
    conexion = sqlite3.connect(database)
    return conexion

def to_list(lead,db = connect_db()):
    cursor = db.cursor()
    consulta = cursor.execute('''SELECT * FROM %s''' % lead)
    for data in consulta:
        print(""" 
        ID :        {}
        NOMBRE :    {}
        EMAIL :     {}
        TELEFONO :  {}
        """.format(data[0],data[1],data[2],data[3]))

def create(lead,db = connect_db()):
    name = str(input("INGRESA SU NOMBRE: "))
    email = str(input("INGRESA SU EMAIL: "))
    tel = str(input("INGRESA SU TELEFONO: "))
    cursor = db.cursor()
    if(len(name) > 0 and len(email) > 0 and len(tel) > 0):
        cursor.execute('''INSERT INTO {} (name,email,tel) VALUES ('{}','{}','{}')'''.format(lead,name,email,tel))
        db.commit()
        print("Insertados")
    else: create(lead)


def update(lead,db = connect_db()):
    try:
        id = int(input("INGRESA EL ID: "))
    except ValueError:
        print("La opción que ingreso no es un numero")
        update(lead)
    else:
        if(id != 0):
            name = str(input("INGRESA SU NOMBRE: "))
            email = str(input("INGRESA SU EMAIL: "))
            tel = str(input("INGRESA SU TELEFONO: "))
            if(len(name) > 0 and len(email) > 0 and len(tel) > 0):
                cursor = db.cursor()
                cursor.execute('''UPDATE {} SET name='{}',email='{}',tel='{}' WHERE id={}'''.format(lead,name,email,tel,id))
                db.commit()
                print("Actualizado!")

def delete(lead,db = connect_db()):
    try:
        id = int(input("INGRESA EL ID: "))
    except ValueError:
        print("La opción que ingreso no es un numero")
        delete(lead)
    else:
        if(id != 0):
            cursor = db.cursor()
            cursor.execute('''DELETE FROM {} WHERE id={}'''.format(lead,id))
            db.commit()
            print("Eliminado!")
        else:
            print("Se require un ID")

def search(lead,db = connect_db()):
    name = str(input("Buscar por nombre: "))
    if(len(name) > 0):
        cursor = db.cursor()
        user = cursor.execute('''SELECT * FROM {} WHERE name like '%{}%' '''.format(lead,name))
        db.commit()
        for data in user:
            print(""" 
            +ID :        {}
            +NOMBRE :    {}
            +EMAIL :     {}
            +TELEFONO:   {}""".format(data[0],data[1],data[2],data[3]))


def Interface():
    while True:
        print("*************************")
        print("**Seleccione una opcion**")
        print("*************************")
        print("** Listar       : 1    **")
        print("** Crear        : 2    **")
        print("** Actualizar   : 3    **")
        print("** Eliminar     : 4    **")
        print("** Buscar       : 5    **")
        print("** Cerrar       : 6    **")
        print("*************************")
        print("*************************")
        try:
            opcion = int(input("Ingresar un numero "))
        except ValueError:
            system("clear")
            print("La opción que ingreso no es un numero")
            Interface()
        else:
            if opcion == 1:
                system("clear")
                to_list(lead)
            elif opcion == 2:
                system("clear")
                create(lead)
            elif opcion == 3:
                system("clear")
                update(lead)
            elif opcion == 4:
                system("clear")
                delete(lead)
            elif opcion == 5:
                system("clear")
                search(lead)
            elif opcion == 6:
                exit()
            else:
                system("clear")
                Interface()

if __name__ == '__main__':
    create_db(database)
    Interface()

import time
import os.path as path
import csv
from datetime import datetime
from random import random

from crate import client

def createDatabase(connection):

    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE coches (id integer primary key, marca text, modelo text, anio int)")
        print("TABLE CREATED")

    except Exception as err:

        print("ERROR CREATING TABLE: %s" % err + "\n")

def insertStatements(connection):

    cursor = connection.cursor()

    try:

        print("Sleeping for 10 seconds...")
        time.sleep(10)

        print("Añadiendo registros de coches a la base de datos... \n")

        cursor.execute("INSERT INTO coches VALUES (1, 'BMW', 'M3', 2021)")
        print("\t INSERT INTO coches VALUES (1, 'BMW', 'M3', 2021)")

        cursor.execute("INSERT INTO coches VALUES (2, 'Ford', 'Focus', 2000)")
        print("\t INSERT INTO coches VALUES (2, 'FORD', 'Focus', 2000)")

        cursor.execute("INSERT INTO coches VALUES (3, 'Mercedes Benz', 'Clase G', 2017)")
        print("\t INSERT INTO coches VALUES (3, 'BMW', 'M3', 2017)")

        cursor.execute("INSERT INTO coches VALUES (4, 'Audi', 'R8', 2019)")
        print("\t INSERT INTO coches VALUES (4, 'Audi', 'R8', 2019)")

        cursor.execute("INSERT INTO coches VALUES (5, 'Daewoo', 'Kalos', 2003)")
        print("\t INSERT INTO coches VALUES (5, 'Daewoo', 'Kalos', 2003)")

        print("\n Se han añadido los registros a la base de datos \n")

    except Exception as err:

        print("INSERT ERROR: %s" % err)

def guardarDatos(result):

    with open('../docker/datos_db.txt', 'w') as fich:
        fich.write(str(datetime.now()) + '\n')
        for element in result:
            fich.write("Registro añadido a la BD: " + str(element) + '\n')

def registroCoches():

    #Creamos la conexión

    try:
        print ("Trying to connect to database...")
        connection = client.connect("http://localhost:4200/", username="crate", timeout=10, error_trace=True,
                                    backoff_factor=0.2)
        print("CONNECTION DONE")

    except Exception as err:
        print("CONNECT ERROR: %s" % err)

    #Eliminamos la tabla, si existiera, para no crear conflicto:

    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS coches;")

    createDatabase(connection)  # Creamos una tabla donde insertar los datos
    insertStatements(connection)  # Insertamos varios registros en la tabla creada

    # Probamos que los datos se han insertado correctamente:

    try:
        print("Sleeping for 10 seconds...")
        time.sleep(10)
        cursor = connection.cursor()
        print("\nEl número de elementos en la BD debería ser 5")
        cursor.execute("SELECT COUNT(*) FROM coches")
        result = cursor.fetchone()
        print("Y el numero de elementos es: " + str(result))
        print("\nLos datos incluidos son: \n")
        cursor.execute("SELECT id, marca, modelo, anio FROM coches order by id")
        result = cursor.fetchall()
        for element in result:
            print("\t" + str(element) + "\n")


    except Exception as err:

        print("\n No se han podido obtener los datos \n")

    # Guardamos los datos en un fichero
    print("Guardando los registros en un fichero...")
    guardarDatos(result)
    print("Registros guardados\n")

    print("Esto ha sido todo. Agur :) \n")

    time.sleep(5)

if __name__ == "__main__":

    registroCoches()

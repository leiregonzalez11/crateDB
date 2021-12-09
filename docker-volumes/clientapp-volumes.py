import time
import os.path as path
import csv
from datetime import datetime
from random import random

from crate import client

def createDatabase(connection):

    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE coches (marca text, modelo text, anio int)")
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

def registroCoches():

    time.sleep(10)

    #Creamos la conexión

    try:
        connection = client.connect("http://localhost:4200/", username="crate", timeout=5, error_trace=True,
                                    backoff_factor=0.2)
        print("CONNECTION DONE")

    except Exception as err:
        print("CONNECT ERROR: %s" % err)

    createDatabase(connection)  # Creamos una tabla donde insertar los datos
    insertStatements(connection)  # Insertamos varios registros en la tabla creada

    # Probamos que los datos se han insertado correctamente:

    try:
        print("Sleeping for 10 seconds...")
        time.sleep(10)
        cursor = connection.cursor()
        print("\n El número de elementos en la BD debería ser 5")
        cursor.execute("SELECT COUNT(*) FROM coches")
        result = cursor.fetchone()
        print("Y el numero de elementos es: " + str(result))
        print(" Los datos incluidos son: \n")
        cursor.execute("SELECT id,marca,modelo,anio FROM coches order by id")
        result = cursor.fetchall()
        for element in result:
            print("\t" + str(element) + "\n")

    except Exception as err:

        print("\n No se han podido obtener los datos \n")

        # Ahora crearemos una tabla donde añadiremos cada 10 segundos un numero aleatorio.

    try:
        print("CREATE TABLE numero (numero int, datetime text)")
        print("TABLE CREATED")

    except Exception as err:
        print("ERROR CREATING TABLE: %s" % err + "\n")

    if not path.exists('DBrows.csv'):
        with open('DBrows.csv', 'w', newline='') as csvfile:
            fieldnames = ['numero', 'datetime']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    while True:

        number = random.randint(1, 10000)
        now = datetime.now()

        cursor.execute("INSERT INTO numero VALUES (?, ?)", number, str(now))

        file = open('DBrows.csv', 'a', newline='')
        file.write("Numero añadido: " + str(number) + " Hora: " + str(now) + "\n")
        file.close()

        time.sleep(30)


if __name__ == "__main__":

    registroCoches()

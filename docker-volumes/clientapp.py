import time
import os.path as path
import csv
from datetime import datetime
from random import random

from crate import client

def createDatabase(cursor):

    try:
        cursor.execute("CREATE TABLE coches (marca text, modelo text, anio int)")
        print("TABLE CREATED")

    except Exception as err:

        print("ERROR CREATING TABLE: %s" % err + "\n")


def insert(cursor):

    try:

        print("Añadiendo registros de coches a la base de datos... \n")

        cursor.execute("INSERT INTO coches VALUES ('BMW', 'M3', 2021)")
        print("INSERT INTO coches VALUES ('BMW', 'M3', 2021)")

        cursor.execute("INSERT INTO coches VALUES ('Ford', 'Focus', 2000)")
        print("INSERT INTO coches VALUES ('FORD', 'Focus', 2000)")

        cursor.execute("INSERT INTO coches VALUES ('Mercedes Benz', 'Clase G', 2017)")
        print("INSERT INTO coches VALUES ('BMW', 'M3', 2017)")

        cursor.execute("INSERT INTO coches VALUES ('Audi', 'R8', 2019)")
        print("INSERT INTO coches VALUES ('Audi', 'R8', 2019)")

        cursor.execute("INSERT INTO coches VALUES ('Daewoo', 'Kalos', 2003)")
        print("INSERT INTO coches VALUES ('Daewoo', 'Kalos', 2003)")

        print("INSERTS DONE \n")
        print("Se han añadido los registros a la base de datos \n")

    except Exception as err:

        print("INSERT ERROR: %s" % err)

def registroCoches():

    time.sleep(10)

    #Creamos la conexión

    try:
        connection = client.connect('crate:4200', timeout=5, error_trace=True, backoff_factor=0.2)
        print("CONNECTION DONE")

    except Exception as err:
        print("CONNECT ERROR: %s" % err)

    cursor = connection.cursor()

    createDatabase(cursor) #Creamos una tabla donde insertar los datos
    insert(cursor) #Insertamos varios registros en la tabla creada

    #Probamos que los datos se han insertado correctamente:

    try:
        time.sleep(10)
        print("El numero de elementos en la BD debería ser 5")
        cursor.execute("SELECT COUNT(*) FROM coches")
        print("Y el numero de elementos en la bd es: " + cursor.fetchall())

    except Exception as err:
        print("No se han podido obtener los datos")

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
            date = now.date()  # coge la fecha de hoy
            hour = now.time().__str__()  # coge la hora exacta

            cursor.execute("INSERT INTO numero VALUES (?, ?)", number, str(now))

            file = open('DBrows.csv', 'a', newline='')
            file.write("Numero añadido: " + str(number) + " Hora: " + str(now) + "\n")
            file.close()

            time.sleep(30)


if __name__ == "__main__":

    registroCoches()
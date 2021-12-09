import sys
import time

from crate import client

def createDatabase(connection):

    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE coches (id integer PRIMARY KEY, marca text, modelo text, anio int)")
        print("TABLE CREATED")

    except Exception as err:

        print("ERROR CREATING TABLE: %s" % err + "\n")


def insert(connection):

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
        connection = client.connect("http://localhost:4200/", username="crate", timeout=5, error_trace=True, backoff_factor=0.2)
        print("CONNECTION DONE")

    except Exception as err:
        print("CONNECT ERROR: %s" % err)


    createDatabase(connection) #Creamos una tabla donde insertar los datos
    insert(connection) #Insertamos varios registros en la tabla creada

    #Probamos que los datos se han insertado correctamente:

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


if __name__ == "__main__":

    registroCoches()

import sys

from crate import client
import requests

def createDatabase(connection):

    cursor = connection.cursor()

    try:
        cursor.execute("""CREATE TABLE usuario (dni varchar(9) PRIMARY KEY NOT NULL,
                                           nombre varchar(25) NOT NULL)""")
        print("DATABASE CREATED")

    except Exception as err:

        print("ERROR CREATING DATABASE: %s" % err + "\n")
        sys.exit(0)


def insert(connection):

    # New connection each time
    cursor = connection.cursor()

    try:

        dni = input("Introduce un DNI \n")
        nombre = input("Introduce un nombre \n")

        if not dniValido(dni):
            print("El DNI introducido no es válido. Adios")
            sys.exit(0)

        elif len(nombre) > 10:
            print("El nombre supera la longitud máxima permitida (10 caracteres). Adios")
            sys.exit(0)
        else:
            cursor.execute("INSERT INTO usuario (dni,nombre) VALUES (?,?)", [dni, nombre],)
            print("INSERT DONE \n")
            print("Se ha añadido el usuario a la base de datos \n")

    except Exception as err:

        print("INSERT ERROR: %s" % err)
        sys.exit(0)


def dniValido(nif):

    #Código obtenido y adaptado de https://discusionesconmipadre.wordpress.com/2010/10/19/comprobar-nif-con-python/

    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    valido = False

    if len(nif) == 9:
        letraControl = nif[8].upper()
        dni = nif[:8]
        if len(dni) == len([n for n in dni if n in numeros]):
            if letras[int(dni) % 23] == letraControl:
                valido = True

    return valido

def registrarUsuario():

    try:
        #connection = client.connect("crate-internal-service:4200")
        connection = client.connect('https://localhost:4200/')
        print("CONNECTION DONE")

    except Exception as err:
        print("CONNECT ERROR: %s" % err)
        sys.exit(0)

    createDatabase(connection)

    insert(connection)

    #Cuenta el numero de usuarios cuyo dni empieza por 79

    cursor = connection.cursor()
    print("Número de usuarios totales:")
    cursor.execute("SELECT COUNT(*) FROM usuario")

    print("Tarea finalizada. Adios :)")
    sys.exit(0)

if __name__ == "__main__":

    registrarUsuario()

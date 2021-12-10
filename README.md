# Aplicación cliente con CrateDB

## ¿Qué es CrateDB? :woman_shrugging:

CrateDB es una base de datos SQL distribuida construida sobre una 
base NoSQL, de código abierto, distribuido y compartido, desarrollado
por Crate.io. Combina la familiaridad de SQL con la escalabilidad y la
flexibilidad de datos de NoSQL, permitiendo a los desarrolladores 
utilizar SQL para procesar cualquier tipo de datos, estructurados o 
no estructurados, realizar consultas SQL a velocidad de tiempo real 
y escalar de forma sencilla. 

## Pre-Requisitos

Tener todos los entornos instalados y funcionando correctamente. En caso de que no estén,
la instalación de estos serán responsabilidad del usuario. Entornos en los que se
realizarán las pruebas:

- Docker
- Kubernetes
- Vagrant

## Instalación :inbox_tray:

El primer paso para la instalación es crear un directorio donde alojar la
aplicación. Después, descargarse el código fuente de este repositorio y extraer
los archivos en el directorio creado. Una vez extraido, accederemos al directorio.


## Ejecución de la aplicación con Docker :arrow_forward:

Antes de nada, accederemos a la carpeta que contiene los ficheros docker
para poder ponerlos en ejecución

    cd docker

Para ejecutar la aplicación, utilizaremos el siguiente comando:

    docker-compose up --build -d

De esta manera, se crearán los contenedores en segundo plano. Para comprobar que
se han creado, podemos utilizar el siguiente comando:

    docker ps

Se mostrarán los contenedores que están activos en este momento, entre los que
deberían estar los contenedores creados en el paso anterior. Si todo ha ido bien, ahora podemos probar nuestra aplicación. 
Para ello, ejecutaremos el siguiente comando:

    python3 clientapp.py

Si se quiere ver cómo se crea la tabla y se añaden los registros, se puede ver en el
siguiente enlace: https://localhost:4200

Para detener la ejecución de los contenedores, simplemente ejecutar:

    docker-compose down

## Ejecución de la aplicación con Kubernetes :computer:

## Ejecución de la aplicación con Vagrant (desde Windows) :pick: 

Primero de todo, y al igual que hemos hecho con docker, accederemos al directorio
donde se encuentran los ficheros vagrant:

    cd ..
    cd vagrant

Después, para poner en marcha el Vagrant file, simplemente hacer:

    vagrant up

Cuando esté en ejecución, podemos acceder a la máquina y ejecutar nuestra aplicación cliente:
    
    vagrant ssh
    python3 clientapp.py

Para detener la ejecución, simplemente hacer CTRL+C. Para apagar la máquina, ejecutar:

    vagrant halt


## NOTA IMPORTANTE :bangbang:

En caso de que por alguna razón mediante Docker no funcionase la aplicación,
se puede probar realizando los siguientes pasos:

Ejecutar en una terminal:

    docker run -–publish 4200:4200 -–publish 5432:5432 crate -Cdiscovery.type=single-node

En otra terminal, ejecutar nuestra aplicación cliente (desde el directorio donde está la app):
    
    python3 clientapp.py

## Autor

:woman_student: Leire Gonzalez Lopez


:books: Proyecto realizado para la asignatura **Administración de Sistemas** del grado en Ingeniería Informatica
de Gestión y Sistemas de Información de la Escuela de Ingeniería de Bilbao, UPV/EHU.

:man_teacher: Profesor: Unai López Novoa

## Más información

Para más información, visitar la página web oficial: https://crate.io/products/cratedb







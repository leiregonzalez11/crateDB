# Aplicación con CrateDB

## ¿Qué es CrateDB? :woman_shrugging:

CrateDB es una base de datos SQL distribuida construida sobre una 
base NoSQL, de código abierto, distribuido y compartido, desarrollado
por Crate.io. Combina la familiaridad de SQL con la escalabilidad y la
flexibilidad de datos de NoSQL, permitiendo a los desarrolladores 
utilizar SQL para procesar cualquier tipo de datos, estructurados o 
no estructurados, realizar consultas SQL a velocidad de tiempo real 
y escalar de forma sencilla. 

## Instalación :inbox_tray:

El primer paso para la instalación es crear un directorio donde alojar la
aplicación. Después, descargarse el código fuente de este repositorio y extraer
los archivos en el directorio creado. Una vez extraido, accederemos al directorio.


## Ejecución de la aplicación con Docker :arrow_forward:

Para ejecutar la aplicación, utilizaremos el siguiente comando:

    docker-compose up --build -d

De esta manera, se crearán los contenedores en segundo plano. Para comprobar que
se han creado, podemos utilizar el siguiente comando:

    docker ps

Se mostrarán los contenedores que están activos en este momento, entre los que
deberían estar en el paso anterior. Si todo ha ido bien, ahora podemos probar nuestra aplicación. 
Para ello, ejecutaremos el siguiente comando:

    python3 clientapp.py


## NOTA IMPORTANTE :bangbang:

En caso de que por alguna razón mediante Docker no funcionase la aplicación,
se puede probar realizando los siguientes pasos:

Ejecutar en una terminal:

    sudo docker run –-publish=4200:4200 --publish=5432:5432 crate

En otra terminal, ejecutar nuestra aplicación cliente (desde el directorio donde está la app):
    
    python3 clientapp.py

## Autor 

:woman_student: Leire Gonzalez Lopez








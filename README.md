# Prueba técnico
Proyecto realizado en python y mongodb para prueba técnico

Requisitos:
 * Docker
 * Docker-compose

# Tecnologias
* Python 3.7
* Flask 1.0
* mongodb

# Instalación
Creamos los contenedores
```bash
docker-compose build
```

Levantamos la aplicacion
```bash
docker-compose up -d
```

Cargamos la bbdd con datos de la API https://swapi.co/
```bash
docker-compose exec web flask create-data
```

Una vez finalizado podremos acceder al front de la aplicacion:

http://localhost:5000

Consumir los datos con la API

http://localhost:5000/api/films/

http://localhost:5000/api/peoples/
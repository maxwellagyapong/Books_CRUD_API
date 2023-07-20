# Loan Application Project
Simple django application with CRUD as main features

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Commands](#commands)
* [App endpoints](#app-endpoints)
* [API Documentation](#api-documentation)


## General info
Simple django application with CRUD as main features


## Technologies
* Python
* Django
* Django Rest Framework
* Docker
* PostgreSQL

### Setup
## Installation on Linux and Mac OS
* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](https://docs.docker.com/engine/install/) on how to install and run docker
* To run application with docker
```
docker-compose up --build
```
  
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at http://0.0.0.0:8000).
* Open the address in the browser

## Commands
Open docker bash with 
```
docker ps
docker exec -it <CONTAINER_NAME> bash
```
In our case, default container name is "crud"
* To run migrations
```
python manage.py makemigrations
python manage.py migrate

```
* To run query_script. This creates the necessary tables in the db and populate it with data from books.csv file and also output results of various queries to console. 
```
python manage.py query_script
```

## App Endpoints
* /books - returns the list of all saved books 
* /books/<int:pk> - return a specific book based on the primary key passed

<!-- ## API Documentation
```
http://127.0.0.1:8000/doc
``` -->
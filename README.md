# Virtual Environment + DJango Lesson
## [Dev.f GDL](https://www.devf.mx/guadalajara) - Cinta Negra - Batch 1
-----------------

**Installation:**
-----------------

```
#> pip install virtualenv  --> Install virtualenv
#> virtualenv <environment-name>
```

To run the Environment is:

- **Mac/Unix**
source bin\activate

- **Win**
Scripts/activate.bat

```
(Environment)>   --> This is how the Terminal should looks like when activated, run the commands inside this 'context'

(Environment)> pip install django

(Environment)> mkdir <django-app>

(Environment)> django-admin startproject <django-project>  

(Environment)> py manage.py runserver   -> run server

(Environment)> py manage.py startapp <django-app>  -> Create an App (Model?)

(Environment)> py manage.py shell -> Opens the Interactive Shell

```

## DJango Project Environment
-------------------------

settings.py
urls.py
wsgi.py


## Models + Migrations
---------------------

- Make sure you have your DB Connection parameters for your DBMS, Also be sure you have your drivers installed (mysqlclient for mysql)
- Create you model into the app/models.py file
- Append your model into settings.py into INSTALLED_APPS object/array
- Once we have the model, run:

```
(Environment)> py manage.py makemigrations
```

- Once we have the migrations files, we can run it:

```
(Environment)> py manage.py migrate   
```

You can create a model into your Database using the Interactive Shell

```
(Environment)> py manage.py shell
(Interactive Shell)> from <app-name> import *
(Interactive Shell)> <variable> = <app-name>.objects.create({Params}...)
```

## Django DataBase Settings
---------

## Django 

## Requirements PIP
----------

This help us to freeze the dependencies version for PIP to download. This is viable using requirements.txt inside the 
project folder

```
<dependency>[==<version>]
```

Also we need to verify to run first the pip install to avoid installing eveything each time we create/run the container
(git diff Dockerfile):
```
FROM python:3.6
+COPY djangoApp/damnificados/requirements.txt /djangoApp/requirements.txt
+RUN pip install -r requirements.txt
 WORKDIR /djangoApp
 COPY djangoApp/damnificados/ /djangoApp
-
-RUN pip install django
-RUN pip install mysqlclient
-RUN pip install gunicorn
-
 CMD gunicorn --bind 0.0.0.0:8000 damnificados.wsgi:application

```

## Docker Fundamentals 
----------


Docker Images are build based on a file content, filled with instructions to tell docker what to download
what to install and how to install.

Using [Docker Repos](https://hub.docker.com) to store and download official images

### Docker Commands
---------

```
#> docker --version             -> Get version of your docker
#> docker pull <image-name>     -> Download an image from docker hub   
#> docker run <PARAMS>
#> docker ps                    -> Get the list of your active processes (CONTAINER ID, IMAGE, COMMAND, CREATED, STATUS, PORTS, NAMES)
#> docker exec <PARAMS> <image-name> <command>      -> Gets into the Container and executes a command
#> docker rmi <image-id>        -> Deletes an image
#> docker build -t <image-name>:<image-tag> <Dockerfile-path>

```

### Dockerfile
--------

This file contains the instructions to build the base image

```
FROM <image-name>:<image-tag>    -> FROM indicates the base image and the tag used by docker, downloaded from the repo

```

Then we define each of the steps to Build the image like the follow:
```
FROM python:3.6         # Here we specify the image that we will use
WORKDIR /djangoApp      # Here we set a folder to set the image on
COPY djangoApp/damnificados/ /djangoApp     # Here we tell docker where the file are and where to place them

RUN pip install django          # In here we start specifying the dependencies that our image needs to be able to run
RUN pip install mysqlclient
RUN pip install gunicorn

CMD gunicorn --bind 0.0.0.0:8000 damnificados.wsgi:application  # Here we explain the command to RUN the actual service that we need, in this case gunicorn
```

Each step is handled as a a _layer_ and that's because if you make any change to it, docker can do only the new steps and do not download everything else.
This help us to avoid the download of an whole image each time we add a new step

We can link images that will comunicate eachother, for this we use an extra parameter called *--link <service-name>* and we send the service name
that is related to.

### Docker Compose
-------

Since we will use microservices in the near future, we will face a lot of problems to link all of them. To avoid that problem we can use *Docker Compose*.
This tool will help us to create a _Group/Package_ and run all the images linked within the same network, so we do not need to link by hand all the different images.

The syntax is the following:

*docker-compose.yml*

```
version: '2' #This is the latest version

services:
  <container-name>: # The first container name that you'll run
    image: <image-name>  # You can use an image directly from hub.docker
    ports:
      - "<port_to:bind>"  # In case you need to bind ports
    depends_on:     # In case your image depends on someone else
      - <container-name>  

  <container-name>:
    build: <path-to-Dockerfile>   # You can also build an local image inside your network
    environment:            # You can set environment variables if needed
      - <environment-variable>   
```

## What this Repo is for ?
It contains source code for tutorial published at
https://medium.com/@mansha99/microservices-in-python-django-rabbitmq-and-pika-fe1adb0c6a1a

### What it demonstrates?
How to create Application following microservice architecture pattern using Django, RabbitMQ and Pika


## I am making it my own but introducing some advanced changes

## how to setup the project
1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. install RebbitMQ
5. Run the services

cd main_service
python manage.py runserver

cd worker_service
 python3 manage.py launch_queue_listener
 
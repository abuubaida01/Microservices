# /home/dragon/projects/microservices/django-rabbitmq-microservice/LogginService/logger/management/commands/launch_queue_listener.py

from django.core.management.base import BaseCommand
from logger.queue_listener import UserCreatedListener


class Command(BaseCommand):
    help = 'Launches Listener for user_created message : RaabitMQ'
    def handle(self, *args, **options):
        td = UserCreatedListener()
        td.start()
        self.stdout.write("Started Logger Consumer Thread")
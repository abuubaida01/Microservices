# /home/dragon/projects/microservices/django-rabbitmq-microservice/LogginService/logger/models.py

from django.db import models

class Log(models.Model):
    action = models.CharField(max_length=255)
    details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} at {self.created_at}"
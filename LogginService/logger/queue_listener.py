# /home/dragon/projects/microservices/django-rabbitmq-microservice/LogginService/logger/queue_listener.py

import json
import pika
import threading
from logger.models import Log

ROUTING_KEY = 'user.created.key'
EXCHANGE = 'user_exchange'
THREADS = 5

class UserCreatedListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=EXCHANGE, exchange_type='direct')
        # self.channel.queue_declare(queue=QUEUE_NAME, auto_delete=False)
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(queue=queue_name, exchange=EXCHANGE, routing_key=ROUTING_KEY)
        self.channel.basic_qos(prefetch_count=THREADS*10)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback)
        
    def callback(self, channel, method, properties, body):
        print("\n properties.content_type", properties.content_type)
        print("\n method", method)
        
        if(properties.content_type=="user_created_method"):
            message = json.loads(body)
            print("\n my message", message)

            # Save the log to the Log table
            Log.objects.create(
                action="user_created",
                details=message
            )

        channel.basic_ack(delivery_tag=method.delivery_tag)
        
    def run(self):
        print ('\n Inside LogginService:  Created Listener ')
        self.channel.start_consuming()
    
   
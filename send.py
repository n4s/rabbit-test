#!/usr/bin/env python
import os
import pika

ip = os.environ['RABBIT_PORT_5671_TCP_ADDR']
print "Connecting to ",ip
connection = pika.BlockingConnection(pika.ConnectionParameters(ip))
channel = connection.channel()
channel.queue_declare(queue='test')

channel.basic_publish(exchange='', routing_key='test', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()

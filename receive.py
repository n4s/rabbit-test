#!/usr/bin/env python
import os
import pika

# callback routine
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

ip = os.environ['RABBIT_PORT_5671_TCP_ADDR']
print "Connecting to ",ip
connection = pika.BlockingConnection(pika.ConnectionParameters(ip))
channel = connection.channel()
channel.queue_declare(queue='test')

# subscribe to channel
channel.basic_consume(callback, queue='test', no_ack=True)

# wait
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# close
connection.close()

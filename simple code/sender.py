import pika


#create connection to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

#create channel
ch1 = connection.channel()

#create queue named hello
ch1.queue_declare(queue='hello')

#send message in our queue
ch1.basic_publish(exchange='', routing_key='hello', body='Hello World')

#for test purpose
print('Message sent')

#close connection after sent
connection.close()
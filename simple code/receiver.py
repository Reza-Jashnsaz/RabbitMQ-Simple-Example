import pika


#create connection to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

#create channel
ch2 = connection.channel()

#create queue named hello
ch2.queue_declare(queue='hello')

#callback function for execute message from sender
def callback(ch, method, properties, body):
	print(f'Received {body}')


#recieve message in our queue
ch2.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

#for test
print('Waiting for message, to exit press ctrl+c')

#listen to queue
ch2.start_consuming()
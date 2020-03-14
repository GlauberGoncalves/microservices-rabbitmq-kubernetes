import pika
import json
import os

def create_connection():
    credentials = pika.PlainCredentials(os.getenv("RABBITMQ_DEFAULT_USER"), os.getenv("RABBITMQ_DEFAULT_PASS"))
    parameters = pika.ConnectionParameters(os.getenv("RABBITMQ_DEFAULT_HOST"),
                                   os.getenv("RABBITMQ_DEFAULT_PORT"),
                                   os.getenv("RABBITMQ_DEFAULT_VHOST"),
                                   credentials)
    
    return pika.BlockingConnection(parameters)
    
def notify(payload):
    conn = create_connection()
    
    channel = conn.channel()
    
    # TODO: Verificar se essa linha realmente é importante
    # ou se da para enviar mensagens sem declarar a queue
    #channel.queue_declare(queue=queue)

    channel.queue_declare(queue='checkout_ex')
    channel.basic_publish(exchange='',
                        routing_key='checkout_ex',
                        body=json.dumps(payload, default=dumper, indent=2))

    print(" [x] Mensage Sent '{}'".format(payload))
    
    conn.close()


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

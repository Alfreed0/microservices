from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

conf = {'bootstrap.servers': 'localhost:9092'}

producer = Producer(conf)

topic = 'testing'
partition = 0
key = None
message = 'Yo! Testing consumer and producer for Siemav microservice'
producer.produce(topic, key=key, value=message, partition=partition, callback=delivery_report)

producer.poll(1)

producer.flush()
from confluent_kafka import Consumer, KafkaException, TopicPartition

conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'my_consumer_group',
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)

topic = 'testing'
partition = 0
offset = 0

# consumer.subscribe([topic])
tp = TopicPartition(topic, partition, offset)
consumer.assign([tp])

try:
    while True:
        msg = consumer.poll(timeout=1000)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        print('Received message: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass
finally:
    consumer.close()

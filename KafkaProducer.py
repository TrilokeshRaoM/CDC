from kafka import KafkaProducer

bootstrap_servers = ['localhost:29092']
topicName = 'testCDC1'

try:
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    future = producer.send(topicName, b'Hello!')
    result = future.get(timeout=60)
except Exception as e:
    print(f"Exception occurred: {e}")
else:
    print(f"Message sent successfully to topic {result.topic}, partition {result.partition}, with offset {result.offset}")
finally:
    producer.close()

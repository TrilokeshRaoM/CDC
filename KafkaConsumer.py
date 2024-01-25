from kafka import KafkaConsumer

bootstrap_servers = ['localhost:29092']

topicName = 'testCDC1'

consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers = bootstrap_servers,auto_offset_reset='earliest')

for msg in consumer:
    print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))

from kafka import KafkaConsumer

if __name__=="__main__":
    consumer=KafkaConsumer("test",bootstrap_servers=['localhost:9092'],auto_offset_reset="earliest",group_id="consumer-a")
    print("Consumer started")
    for i in consumer:
        print(i)

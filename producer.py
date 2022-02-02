from kafka import KafkaProducer
import json
import data
import time
def json_serializer(val):
    return json.dumps(val).encode("utf-8")

val={
    "name":"baba",
    "age":2000
}

op=json_serializer(val)
producer=KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=json_serializer)

if __name__=="__main__":
    i=0
    while 1==1:
        producer.send('test',data.get_registered_user())
        i+=1
        print("iteration:",str(i))
        print(data.get_registered_user())
        time.sleep(5)
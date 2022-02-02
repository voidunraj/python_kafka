# python_kafka
Simple Stepwise setup for Apache Kafka with Concepts explained in Python

Apache Kafka can be obtained from the https://kafka.apache.org/downloads look for the most recent version. This is the open sourced version of Kafka from Apache , but most of the organisations use Confluent Kafka or a version which is of Enterprise level implementation nature.

In Simple words pass on the risk and headache of maintaining the software to an outside vendor and focus on only building what is needed for your Software Project. 

In this repository will focus on the Apache Kafka , should be a similar implementation for Confluent Kafka.

Step1 : Download the .tgz file from the Apache Kafka website

Step2 : run the command tar -xvzf <kafka.tgz>
For example $tar -xvzf kafka-3.0.0-src.tgz > there is a problem with 3.0.0 with windows sometime use the 2.8.1 version
This will get you the Kafka software in a folder

Step3: Setting up Zookeeper and Start Zookeeper
Look for bin folder and config folder , the command can be run as is if you have not done any modification
If Unix run the below 

$zookeeper-server-start.sh ../config/zookeeper.properties

If Windows look for the bat folder look for hte .bat scripts to start the zookeeper service
>zookeeper-server-start.bat ..\..\config\zookeeper.properties

Yes we blindly executed this . What does it do .. it will start the zookeeper with default settings with client port as clientPort=2181

Now this is still the zookeeper service, not Kafka.

Step4: Starting the Kafka Server
From the config folder lookup server.properties and modify to the below
advertised.listeners=PLAINTEXT://localhost:9092
zookeeper.connect=localhost:2181 -> Remember the config we did above this step see the config matching.

Windows
>kafka-server-start.bat ..\..\config\server.properties


Create a topic
Windows
>kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
Unix
> 

List topics
Unix
>kafka-topics.sh --list --zookeeper localhost:2181
windows
> kafka-topics.bat --list --zookeeper localhost:2181


Run producer.py from command prompt and also keep observing the Kafka Server logs. The place where we started this from will print in the Iteration and data
iteration: 1
{'name': 'baba', 'age': 2000}
iteration: 2
{'name': 'baba', 'age': 2000}
iteration: 3
{'name': 'baba', 'age': 2000}

Run consumer.py from command prompt and also keep observing the Kafka Server logs. The place where we started this from will print the message. 

Consumer started
ConsumerRecord(topic='test', partition=0, offset=0, timestamp=1643770200543, timestamp_type=0, key=None, value=b'{"name": "baba", "age": 2000}', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=29, serialized_header_size=-1)
ConsumerRecord(topic='test', partition=0, offset=1, timestamp=1643770205547, timestamp_type=0, key=None, value=b'{"name": "baba", "age": 2000}', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=29, serialized_header_size=-1)
ConsumerRecord(topic='test', partition=0, offset=2, timestamp=1643770210553, timestamp_type=0, key=None, value=b'{"name": "baba", "age": 2000}', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=29, serialized_header_size=-1)

Note the serialization of the data in the aboce
# docker-kafka-zookeeper-mongo-ui
Multi kafka and zookeeper topics clustering to mongodb
----------------------------------------------------------------------------
 - @name.   docker-compose.yml
 - @author. haeun kim
 - @date.   2023-07-14
 - @title.  Multi kafka and zookeeper topic clustering to mongodb
 - @keywords.  kafka / zookeeper / mongodb / docker


![캡처](/arch-docker-kafka-zookeeper-mongo-ui.png)
 
# Summary Docker containors and ports
### NODE

- 1.ZOOKEEPER         (2) zoo1:2181 | zoo2:2182 
- 2.KAFKA             (2) broker1:29091  |  broker2:29092     
- 3.SCHEMA REGISTRY   (1) schemaregistry:8081
- 4.KSQL              (2) ksqlserver:8088, ksqlcli  
---------------------------------------------------------------------------
### DB                    ... config-replica.js

- 5.MongoDB Replica   (3) mongo1:27017[M] | mongo2:27018[R1] | mongo3:27019[R2]     
- 6.MongoDB Pool      (1) mongo1-setup
---------------------------------------------------------------------------
### Topic & Transaction   .../utils/*  

- 7.CONNECT               8083
- 8.CONTROL               9021
- 9.REST PROXY        (1) restproxy:8082
---------------------------------------------------------------------------
### OPTION

- 10.KAFKA -- UI      (4) topics:8000
- 11.KAFAK TOPIC CREATE
- 12.NETWORKS         (2) localnet:bridge
- 13.VOLUMES
---------------------------------------------------------------------------
### [Connector/Topic] REGISTER & GENERATOR ... /utils file description 

[Connector] CONNECT) 
```
cx simplesink.js
cx simplesource.js
```
[Topic] REST PROXY)  
```
python3 kafkaRest.py
python3 kafkaRestCustom1.py
python3 kafkaRestCustom2.py
python3 kafkaRestCustom3.py
python3 kafkaRestInfo.py
```
[Topic] KSQL) 
```
python3 ksqlStreamCreate.py
python3 ksqlStreamProd.py
python3 ksqlStreamSub.py
```
[Topic] 
```
python3 kafkawrite.py
python3 kafkaread.py  (kafkaread.py ... insert Topic offect to MONGO DB)
```
---------------------------------------------------------------------------
### Kafka command EX. 
```
$sudo docker-compose exec broker2 kafka-topics --create --topic testdb1.book --bootstrap-server broker2:29092 --replication-factor 1 --partitions 1
$sudo docker-compose exec broker2 kafka-topics --describe --topic testdb1.book --bootstrap-server broker2:29092

$sudo docker exec -it broker1 bash
$kafka-console-producer --topic testdb1.book --broker-list broker:29092
$kafka-console-consumer --topic testdb1.book --bootstrap-server broker:29092 --from-beginning
```
---------------------------------------------------------------------------
### Mongo container access EX.
```
$sudo docker exec -it mongo1 bash
$status
$mongosh

> use <DB name>
> show databases
> db.createUser({user: "user", pwd: "pwd", roles:["root"]});
> db.createCollection("person")
> show collections

> db.person.insert({"nickname":"coding-haniii", "email":"coding-haniii@github.com"})
> db.person.find()
```
---------------------------------------------------------------------------
### Ksql-Cli container access EX.
```
$sudo docker exec -it ksqlcli ksql http://localhost:8088
$sudo docker run --net=host --interactive --tty confluentinc/cp-ksql-cli:5.3.0 http://localhost:8088

ksql> version
ksql> show topics;
ksql> show tables;
ksql> CREATE STREAM stream01 (id VARCHAR, time VARCHAR, no int) WITH (kafka_topic='my-topic1', value_format='json', partitions=1);
ksql> select * from stream01;   (consumer)    <--- this must be empty at first time. keep staying on the screen and open another ksql-cli sceen.
1689846118218 | null | haeun | 2023-07-20 18:40:10 | 1
1689846123013 | null | haeun | 2023-07-20 18:40:10 | 2
1689846131426 | null | haeun | 2023-07-20 18:40:10 | 3


*** another ksql-cli open
INSERT INTO stream01 (id, time, no) VALUES ('haniii', '2023-07-20 18:40:10', 1);
INSERT INTO stream01 (id, time, no) VALUES ('haniii', '2023-07-20 18:40:10', 2);
INSERT INTO stream01 (id, time, no) VALUES ('haniii', '2023-07-20 18:40:10', 3);
```
###### *pip install ksql
---------------------------------------------------------------------------
# Ref. 
- https://github.com/confluentinc/cp-demo/blob/7.4.0-post/docker-compose.yml
- https://github.com/mongodb/mongo-kafka/blob/master/docker/docker-compose.yml
- https://github.com/mongodb-university/kafka-edu.git
- https://github.com/provectus/kafka-ui
- https://docs.ksqldb.io/en/latest/reference/processing-log/
- https://stackoverflow.com/questions/64865361/docker-compose-create-kafka-topics
- https://yooloo.tistory.com/109  (ksql, Korean)

###### restart option ->     restart: unless-stopped/always
###### KAFKA_CREATE_TOPICS: "Topic1:2:3,Topic2:1:1"  --> Topic1 partition 2, replica 3 
###### ZOOKEEPER_SSL_* --> search this options! for ssl
###### KAFKA_ZOOKEEPER_SSL_* 

# Good luck!!! :D

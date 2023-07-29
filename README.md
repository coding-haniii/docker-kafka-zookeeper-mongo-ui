# docker-kafka-zookeeper-mongo-ui
Multi kafka and zookeeper topics clustering to mongodb
#############################################################################
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
cx, simplesource.json, simplesink.json
```
[Topic] REST PROXY)  
```
kafkaRest.py, kafkaRestConsum1.py, kafkaRestConsum2.py,kafkaRestConsum3.py, kafkaRestInfo.py
```
[Topic] KSQL) 
```
ksqlStreamCreate.py, ksqlStreamProd.py, ksqlSreamSub.py
```
[Topic] 
```
kafkawrite.py, kafkaread.py  (kafkaread.py ... insert Topic offect to MONGO DB)
```
---------------------------------------------------------------------------
# Ref. 
- https://github.com/confluentinc/cp-demo/blob/7.4.0-post/docker-compose.yml
- https://github.com/mongodb/mongo-kafka/blob/master/docker/docker-compose.yml
- https://github.com/mongodb-university/kafka-edu.git
- https://github.com/provectus/kafka-ui
- https://docs.ksqldb.io/en/latest/reference/processing-log/
- https://stackoverflow.com/questions/64865361/docker-compose-create-kafka-topics

###### restart option ->     restart: unless-stopped/always
###### KAFKA_CREATE_TOPICS: "Topic1:2:3,Topic2:1:1"  --> Topic1 partition 2, replica 3 
###### ZOOKEEPER_SSL_* --> search this options! for ssl
###### KAFKA_ZOOKEEPER_SSL_* 

# Good luck!!! :D

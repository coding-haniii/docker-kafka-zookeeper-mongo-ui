# docker-kafka-zookeeper-mongo-ui
Multi kafka and zookeeper topics clustering to mongodb
#############################################################################
 - @name.   docker-compose.yml
 - @author. haeun kim
 - @date.   2023-07-14
 - @title.  Multi kafka and zookeeper topic clustering to mongodb
 - @keywords.  kafka / zookeeper / mongodb / docker

# Summary containors and ports
#############################################################################

 *NODE
- 1.ZOOKEEPER         (3) zookeeper1:2181 | zookeeper2:2182 | zookeeper3:2183
- 2.KAFKA             (3) broker:9092  |  broker1:9091   | borker2:9092   
- 3.SCHEMA REGISTRY   (1) schemaregistry:8081
- 4.KSQL              (2) ksqlserver:8088, ksqlcli  
---------------------------------------------------------------------------
 *DB            ... config-replica.js
- 5.MongoDB Replica   (3) mongo1:27015[M]     
- 6.MongoDB Pool      (3) mongo-setup
---------------------------------------------------------------------------
 *TRANSACTION   .../utils/*  
- 7.CONNECT               8083
- 8.CONTROL               9021
- 9.REST PROXY        (1) restproxy:8082
---------------------------------------------------------------------------
 *OPTION
- 10.KAFKA -- UI      (4) topics:8000  
- 11.KAFAK TOPIC CREATE
- 12.NETWORKS         (2) localnet:bridge
- 13.VOLUMES
#############################################################################
# Ref. 
#############################################################################
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

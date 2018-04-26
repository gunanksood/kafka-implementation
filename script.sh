#!/bin/bash
#docker run -d \
#    --net=host \
#    --name=zookeeper \
#    -e ZOOKEEPER_CLIENT_PORT=32181 \
#    confluentinc/cp-zookeeper:3.1.1
#
#docker run -d     --net=host     --name=zookeeper     -e ZOOKEEPER_CLIENT_PORT=32181     confluentinc/cp-zookeeper:3.1.1
#
#docker run -d \
#    --name=kafka \
#    -p 29092:29092 \
#    -e KAFKA_ZOOKEEPER_CONNECT=localhost:32181 \
#    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:29092 \
#    confluentinc/cp-kafka:3.1.1
#
#docker run -d     --net=host     -p 29092:9092     --name=kafka     -e KAFKA_ZOOKEEPER_CONNECT=localhost:32181     -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:29092     confluentinc/cp-kafka:3.1.1
#
#docker run -d     --net=bridge     -p 29092:29092     --name=kafka     -e KAFKA_ZOOKEEPER_CONNECT=172.17.0.2:32181     -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:29092     confluentinc/cp-kafka:3.1.1
#
#
#docker run -d     --net=bridge     -p 29092:29092     --name=kafka     -e KAFKA_ZOOKEEPER_CONNECT=172.17.0.2:32181     -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://192.168.101.121:29092     confluentinc/cp-kafka:3.1.1
#
#python produce_example.py localhost 29092
#python produce_example_2.py localhost 29092
#python produce_example_3.py localhost 29092
sudo pip install confluent-kafka
python consume_example.py 192.168.106.144 29092
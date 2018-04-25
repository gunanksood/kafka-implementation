#!/bin/bash
sudo docker run -d \
    --net=host \
    --name=zookeeper \
    -e ZOOKEEPER_CLIENT_PORT=32181 \
    confluentinc/cp-zookeeper:3.1.1

docker run -d \
    --net=host \
    --name=kafka \
    -e KAFKA_ZOOKEEPER_CONNECT=localhost:32181 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:29092 \
    confluentinc/cp-kafka:3.1.1

python consume_example.py localhost 29092
python produce_example.py localhost 29092
python produce_example_2.py localhost 29092
python produce_example_3.py localhost 29092

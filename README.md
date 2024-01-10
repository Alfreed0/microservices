# Microservices Kafka Producer and Consumer
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-000?style=for-the-badge&logo=apachekafka)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

This project is a simple example of how to use Kafka with Zookeper for future implementations.

## Images
1. [Bitanami/kafka](https://hub.docker.com/r/bitnami/kafka)
2. [Bitnami/zookeeper](https://hub.docker.com/r/bitnami/zookeeper)
3. [Zookeeper](https://hub.docker.com/_/zookeeper)

## Confluent Documentation
Prior implementing new code for this project, read the [Confluent Documentation](https://docs.confluent.io/kafka-clients/python/current/overview.html) to understand how to use confluent for consumer and producer basic knowledge.

## How to run
1. Clone this repository
2. Run `docker-compose up -d` to start the containers
3. Run `python3 producer.py` to start the producer
4. Run `python3 consumer.py` to start the consumer


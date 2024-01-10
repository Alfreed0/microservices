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

### Partitions

In the Kafka architecture, topics play a crucial role as they are organized into partitions, each representing an ordered and unchangeable sequence of messages. This partitioning mechanism serves as the backbone for Kafka's horizontal scalability, enabling efficient handling of substantial data volumes by distributing the workload across multiple brokers.
As data is produced into Kafka topics, producers target specific partitions for message storage. Simultaneously, consumers are designed to retrieve and process messages from designated partitions. This partition-centric approach contributes to the parallelization and optimization of data handling within the Kafka ecosystem.
The decision on the number of partitions for a given topic is a fundamental aspect of topic creation. Typically established at the inception of a topic, this configuration often remains static throughout the topic's lifecycle. The fixed partitioning scheme ensures consistency in data distribution and helps maintain a well-organized and efficient Kafka data pipeline.

### Replication
Replication, an integral aspect of Kafka's architecture, involves the creation and distribution of copies (replicas) of partitions across multiple brokers. This process delivers several key benefits:
Fault Tolerance and High Availability: By having replicas distributed across brokers, Kafka ensures fault tolerance. If a broker fails, another with a replica of the partition can seamlessly take over, contributing to high availability.
Backup Mechanism: Replicas are not directly involved in reading or writing operations. Instead, they serve as backup copies, safeguarding data integrity and facilitating recovery in case of unexpected events.
Configurable Redundancy: The number of replicas for a partition is configurable, allowing for flexibility in addressing specific use cases. It is common to have multiple replicas (e.g., 2 or 3) for each partition to enhance fault tolerance and data durability.

### Offset
Offsets play a crucial role in Kafka's messaging model, providing a unique identifier for each message within a partition. This concept is instrumental in managing the position of consumers and ensuring data consistency:
Position Tracking: Offsets are employed to keep track of a consumer's position within a partition. Each message is assigned a unique offset, enabling precise tracking of consumption progress.
Offset Commitment: Consumers commit their current offset to Kafka after processing a message. This commitment allows them to resume consumption from the last processed message in case of restarts, ensuring continuity and consistency.
Configurable Retention: Kafka retains messages for a configurable retention period, and consumers can fetch messages from a specific offset. This flexibility allows tailored approaches to data retrieval based on individual requirements.

### Consumer Groups
Consumer groups are a fundamental concept in Kafka's messaging model, enabling scalability and parallel processing of data. A consumer group is a set of consumers sharing a common group identifier. Each consumer within the group is assigned a subset of partitions from the subscribed topics. This partition assignment ensures that each message is consumed by only one consumer within the group, enabling parallel processing of data. The number of consumers within a group can be scaled up or down based on the workload, allowing for efficient resource utilization and load balancing.

## How to run
1. Clone this repository
2. Run `docker-compose up -d` to start the containers
3. Run `python3 producer.py` to start the producer
4. Run `python3 consumer.py` to start the consumer


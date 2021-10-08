# KRaft mode Kafka on Kubernetes

Resources for a tutorial that covers running KRaft mode Kafka v2.8 on a Minikube-based Kubernetes cluster.

## Tutorial

The tutorial for this project is available [here](https://developer.ibm.com/tutorials/kafka-in-kubernetes) on [IBM Developer](https://developer.ibm.com/) (and possibly cross-posted on other sites).

## Contents

Instructions for how to use this repo are found in the tutorial (links above).

- [docker](docker/): kafka Dockerfile and entrypoint shell script
- [kubernetes](kubernetes/): kubernetes cluster config files managed by minikube



To  produce and consume a topic
Console producer:

kafka-console-producer.sh \
  --topic orders \
  --bootstrap-server broker:9092 \
  --property parse.key=true \
  --property key.separator=":"
Console consumer:

kafka-console-consumer.sh \
  --topic orders \
  --bootstrap-server broker:9092 \
  --from-beginning \
  --property print.key=true \
  --property key.separator="-"

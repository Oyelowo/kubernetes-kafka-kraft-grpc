# KRaft mode Kafka on Kubernetes

Resources for a tutorial that covers running KRaft mode Kafka v3.0.0 on a Minikube-based Kubernetes cluster.

1. Get into one of the kafka pods
`kubectl exec -it kafka-0 -- /bin/bash`

2. Create 
`kafka-topics.sh --create --topic test --partitions 3 --replication-factor 3 --bootstrap-server localhost:9092`

3. Check the configuration 
`kafka-topics.sh --describe --topic test --bootstrap-server localhost:9092`

4. Test inside the pods
```
kafka-console-producer.sh \
  --topic orders \
  --bootstrap-server broker:9092 \
  --property parse.key=true \  // optional
  --property key.separator=":"  // optional
```

In another terminal
Console consumer:
```
kafka-console-consumer.sh \
  --topic orders \
  --bootstrap-server broker:9092 \
  --from-beginning \
  --property print.key=true \
  --property key.separator="-"
```

## Tutorial

The tutorial for this project is available [here](https://developer.ibm.com/tutorials/kafka-in-kubernetes) on [IBM Developer](https://developer.ibm.com/) (and possibly cross-posted on other sites).

## Contents

Instructions for how to use this repo are found in the tutorial (links above).

- [docker](docker/): kafka Dockerfile and entrypoint shell script
- [kubernetes](kubernetes/): kubernetes cluster config files managed by minikube



To  produce and consume a topic
Console producer:


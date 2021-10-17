#!/bin/bash

NODE_ID=${HOSTNAME:6}
LISTENERS="PLAINTEXT://:9092,CONTROLLER://:9093"
ADVERTISED_LISTENERS="PLAINTEXT://kafka-$NODE_ID.$SERVICE.$NAMESPACE.svc.cluster.local:9092"

CONTROLLER_QUORUM_VOTERS=""
for i in $( seq 0 $REPLICAS); do
    if [[ $i != $REPLICAS ]]; then
        CONTROLLER_QUORUM_VOTERS="$CONTROLLER_QUORUM_VOTERS$i@kafka-$i.$SERVICE.$NAMESPACE.svc.cluster.local:9093,"
    else
        CONTROLLER_QUORUM_VOTERS=${CONTROLLER_QUORUM_VOTERS::-1}
    fi
done

mkdir -p $SHARE_DIR/$NODE_ID

if [[ ! -f "$SHARE_DIR/cluster_id" && "$NODE_ID" = "0" ]]; then
    CLUSTER_ID=$(kafka-storage.sh random-uuid)
    echo $CLUSTER_ID > $SHARE_DIR/cluster_id
else
    CLUSTER_ID=$(cat $SHARE_DIR/cluster_id)
fi

sed -e "s+^node.id=.*+node.id=$NODE_ID+" \
-e "s+^controller.quorum.voters=.*+controller.quorum.voters=$CONTROLLER_QUORUM_VOTERS+" \
-e "s+^listeners=.*+listeners=$LISTENERS+" \
-e "s+^advertised.listeners=.*+advertised.listeners=$ADVERTISED_LISTENERS+" \
-e "s+^log.dirs=.*+log.dirs=$SHARE_DIR/$NODE_ID+" \
/opt/kafka/config/kraft/server.properties > server.properties.updated \
&& mv server.properties.updated /opt/kafka/config/kraft/server.properties

kafka-storage.sh format -t $CLUSTER_ID -c /opt/kafka/config/kraft/server.properties

exec kafka-server-start.sh /opt/kafka/config/kraft/server.properties


child=$!
echo "==> ✅ Kafka server started.";

kafka_addr="SERVICE.$NAMESPACE.svc.cluster.local:9092"

if [ -z $KRAFT_CREATE_TOPICS ]; then
    echo "==> No topic requested for creation.";
else
    echo "==> Creating topics...";
    chmod +x ./wait-for-it.sh

    ./wait-for-it.sh $kafka_addr;

    pc=1
    if [ $KRAFT_PARTITIONS_PER_TOPIC ]; then
        pc=$KRAFT_PARTITIONS_PER_TOPIC
    fi

    existing_topics=$(kafka-topics.sh --list --bootstrap-server $kafka_addr)
    for i in $(echo $KAFKA_TOPICS | sed "s/,/ /g")
        if [[ " $existing_topics " =~ .*\ $i\ .* ]]; then
            echo "Topic $i already exists";
        else
            ./bin/kafka-topics.sh --create --topic "$i" --partitions "$pc" --replication-factor $KAFKA_REPLICATION_FACTOR --bootstrap-server $kafka_addr;
        fi
    do
    done
    echo "==> ✅ Requested topics created.";
fi


wait "$child";


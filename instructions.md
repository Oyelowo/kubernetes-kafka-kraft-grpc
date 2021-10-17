Generate code from protobuf
`python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ protobuf/person.proto`

For  person Service
`python3 -m grpc_tools.protoc -I./ --python_out=./modules/person/app --grpc_python_out=./modules/person/app/ protobuf/person.proto`

This will generate protobuf code from the .proto file into `./modules/person/`

For Location Service
`python3 -m grpc_tools.protoc -I./ --python_out=./modules/location/app --grpc_python_out=./modules/location/app/ protobuf/person.proto`

This will generate protobuf code from the .proto file into `./modules/location/`

For the main API. Generate all protos. Notice the asterik at the end?
`python3 -m grpc_tools.protoc -I./ --python_out=./modules/location/app --grpc_python_out=./modules/location/app/ protobuf/*`

This will generate protobuf code from the .proto file into `./modules/location/`


# Local development with docker compose
`docker-compose  up --build`

`chmod +x scripts/run_db_docker.sh`


`scripts/run_db_docker.sh postgres-container`


- Send request to the grpc server 
  `python3 client.py`
  `python3 modules/api_person/app/client.py`



api image

oyelowo/udaconnect-app
oyelowo/udaconnect-api
oyelowo/udaconnect-api-person



DB
while in the container

`psql "dbname=person host=localhost user=ct_admin password=wowiamsosecure% port=5432"`


For location 

`kubectl exec -it postgres-location-0 -- /bin/bash`
`psql "dbname=location host=localhost user=ct_admin password=wowiamsosecure% port=5432"`



Test api
```

curl -X GET "http://localhost:30001/api/persons/5" -H "accept: application/json"

curl -X GET "http://localhost:30001/api/persons/1/connection?distance=5&end_date=2022-10-01&start_date=2020-01-01" -H "accept: application/json"

# curl -X POST  -H "Content-Type: application/json" -d '{"first_name": "Oyelowo","last_name":"Oyedayo", "company_name":"Blayz"}' "http://localhost:30001/api/persons"


curl -X POST -H "Content-Type: application/json" \
 -d '{"first_name": "Oyelowo","last_name":"Oyedayo", "company_name":"Blayz"}' \
"http://localhost:30001/api/persons"

```

kubectl delete deployments --all 
kubectl delete statefulsets --all
kubectl delete pods --all 
kubectl delete svc --all 
kubectl delete configmaps --all 

// delete pods with label - service : udaconnect-api-person
kubectl delete po -l "service=udaconnect-api-person"
kubectl delete po -l "service=udaconnect-api-location"

kubectl apply -f deployment/  



Kafka

# KRaft mode Kafka on Kubernetes

Resources for a tutorial that covers running KRaft mode Kafka v3.0.0 on a Minikube-based Kubernetes cluster.

1. Get into one of the kafka pods in namespace - kafka-kraft
`kubectl exec -it kafka-0 -n kafka-kraft -- /bin/bash`
if in default namespace, below should suffice
`kubectl exec -it kafka-0 -- /bin/bash`

1. Create topic named location
`kafka-topics.sh --create --topic location --partitions 3 --replication-factor 3 --bootstrap-server localhost:9092`

3. Check the configuration 
`kafka-topics.sh --describe --topic location --bootstrap-server localhost:9092`

4. Test inside the pods
```
kafka-console-producer.sh \
  --topic location \
  --bootstrap-server localhost:9092 \
  --property parse.key=true \  // optional
  --property key.separator=":"  // optional
```

In another terminal
Console consumer:
```
kafka-console-consumer.sh \
  --topic test \
  --bootstrap-server localhost:9092 \
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





Connecting to a service. 
It's okay to specify just the service name if within the same namespace as the pod/service.

if cross namespace
```
<service_name>.<namespace>
<service_name>.<namespace>.svc
<service_name>.<namespace>.svc.cluster.local
```

 To double-check the last two parts, use CoreDNS as sample, check its configmap:
`kubectl -n kube-system get configmap coredns -o yaml`

From here, I can see the the configuration file for CoreDNS, and could be set to e.g `cluster.local` as port of full DNS name.

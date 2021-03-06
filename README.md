# Instructions

## Application architecture
![Connect App Rearchitecture](./docs/architecture_design.png)
## Running the App in kubernetes
1-5- k3d cluster create oyelowo-cluster-udacon --agents 3 -p "30000-32767:30000-32767@server:0" --kubeconfig-update-default
1-5- `k3d cluster create oyelowo-cluster-udacon --agents 3 -p "30000-30020:30000-30020@server:0" --kubeconfig-update-default`

6- Deploy all resources for the application. This sets up the databases, services and kafka

```sh
kubectl apply -f deployment/
```

7- Check and wait that all pods are running within your cluster

```sh
kubectl get po -A
```

8- Seed the database with some data. This needs to be done only once. This creates location table in location db and person table in person db.
It also creates location kafka topic in kafka
It relies on the name of the statefulsets postgres databases set in kubernetes resource.

```sh
# Make script executable: 
chmod +x ./db/setup_dbs.sh

# Run script:
./db/setup_dbs.sh
```

9- Check list of kafka topics which should only be location topic created within the command above

```sh
kubectl exec -i kafka-0 -n kafka-kraft -- bash -c "kafka-topics.sh --list --bootstrap-server kafka-svc.kafka-kraft.svc.cluster.local:9092"

# or
kubectl exec -i kafka-0 -n kafka-kraft -- bash -c "kafka-topics.sh --list --bootstrap-server localhost:9092"

# You can also subscribe to topic

kubectl exec -i kafka-0 -n kafka-kraft -- bash -c "kafka-console-consumer.sh \
  --topic location \
  --bootstrap-server kafka-svc.kafka-kraft.svc.cluster.local:9092 \
  --from-beginning"
```

## Testing Apis

- Get person with ID of 1

```sh
curl -X GET "http://localhost:30001/api/persons/1" -H "accept: application/json"
```

- Get all connections for person 1 between date
  
```sh
curl -X GET "http://localhost:30001/api/persons/1/connection?distance=5&end_date=2022-10-01&start_date=2020-01-01" -H "accept: application/json"
```

- Create new person

```sh
curl -X POST -H "Content-Type: application/json" \
 -d '{"first_name": "Oyelowo","last_name":"Oyedayo", "company_name":"Blayz"}' \
"http://localhost:30001/api/persons"
```

- Create location
  This sends location payload to the location producer service which is a grpc server that in turn sends the location data formatted as JSON into the `location` kafka topic. This topic is subsequently consumed  the location service which stores the data in the postgres database.

  This was previously handled by the rest API server but has since been changed to handle higher location data traffic.

```sh
python3 modules/location-producer/app/client_test.py 

# You can also send plenty location data for testing:
for i in {1..10000}
    do
    # your-unix-command-here
    echo $i
    python3 modules/location-producer/app/client_test.py 
done

# This does the sending to the GRPC location producer service, e.g
# location_request = location_pb2.CreateLocationRequest(
#     person_id = 1,
#     longitude = "63",
#     latitude = "21",
# )
# response = location_stub.CreateLocation(location_request)
```

__OLD__: _But still works and kept for reference purpose_

```sh
# OLD But still works and kept for reference purpose
# curl -X POST -H "Content-Type: application/json" \
#  -d '{"person_id": 1,"longitude":"24.9384", "latitude":"60.1699"}' \
# "http://localhost:30001/api/locations"

# # You can also send plenty location data for testing:
# for i in {1..10000}
#     do
#     # your-unix-command-here
#     echo $i
#     curl -X POST -H "Content-Type: application/json" \
#     -d '{"person_id": 3,"longitude":"24.9384", "latitude":"60.1699"}' \
#     "http://localhost:30001/api/locations"
# done
```

## Postgres DB client

You can view the databases in a PG client such as PGAdmin or Postico

1- Person DB
    - Host: `localhost`
    - User: `ct_admin`
    - Password: `wowimsosecure`
    - port: `30010`
    - database: `person`

2- Location DB
    - Host: `localhost`
    - User: `ct_admin`
    - Password: `wowimsosecure`
    - port: `30011`
    - database: `location`

## ADDITIONAL

### Generate code from protobuf

- For  person Service

```sh
python3 -m grpc_tools.protoc -I./ --python_out=./modules/person/app --grpc_python_out=./modules/person/app/ protobuf/person.proto
```

This will generate protobuf code from the .proto file into `./modules/person/`

- For Location Service

```sh
python3 -m grpc_tools.protoc -I./ --python_out=./modules/location/app --grpc_python_out=./modules/location/app/ protobuf/*
```

This will generate protobuf code from the .proto file into `./modules/location/`

- For Location Producer Service

```sh
python3 -m grpc_tools.protoc -I./ --python_out=./modules/location-producer/app --grpc_python_out=./modules/location-producer/app/ protobuf/*
```

This will generate protobuf code from the .proto file into `./modules/location-producer/`

- For the main API. Generate all protos. Notice the asterik at the end?

```sh
python3 -m grpc_tools.protoc -I./ --python_out=./modules/api --grpc_python_out=./modules/api/ protobuf/*
```

This will generate protobuf code from the .proto file into `./modules/api/`

## Local development with docker compose

```sh
docker-compose  up --build
```

```sh
chmod +x db-setup-scripts/run_db_docker.sh

db-setup-scripts/run_db_docker.sh postgres-container
```

- Sending request to the grpc server

```sh
python3 client_test.py
python3 modules/api_person/app/client_test.py
```

## Api images

- Frontend app: oyelowo/udaconnect-app
- Main API: oyelowo/udaconnect-api
- Person service: oyelowo/udaconnect-api-person
- Location service: oyelowo/udaconnect-api-location

## Interacting with Postgres databases using PSQL

while in the container e.g for location database

```sh
kubectl exec -it postgres-location-0 -- /bin/bash
psql "dbname=location host=localhost user=ct_admin password=wowiamsosecure% port=5432"
```

For person dabase

```sh
kubectl exec -it postgres-person-0 -- /bin/bash
psql "dbname=person host=localhost user=ct_admin password=wowiamsosecure% port=5432"
```

### Test api

```sh

curl -X GET "http://localhost:30001/api/persons/5" -H "accept: application/json"

curl -X GET "http://localhost:30001/api/persons/1/connection?distance=5&end_date=2022-10-01&start_date=2020-01-01" -H "accept: application/json"


curl -X POST -H "Content-Type: application/json" \
 -d '{"first_name": "Oyelowo","last_name":"Oyedayo", "company_name":"Blayz"}' \
"http://localhost:30001/api/persons"



curl -X POST -H "Content-Type: application/json" \
 -d '{"person_id": 1,"longitude":"24.9384", "latitude":"60.1699"}' \
"http://localhost:30001/api/locations"

```

## Deleting kubernetes resources

```sh
kubectl delete deployments --all 
kubectl delete statefulsets --all
kubectl delete pods --all 
kubectl delete svc --all 
kubectl delete configmaps --all 

# delete pods with label - service : udaconnect-api-person
kubectl delete po -l "service=udaconnect-api-person"
kubectl delete po -l "service=udaconnect-api-location"
```

## Miscellaneous

## Working with Kafka 3.0.0: KRaft mode Kafka on Kubernetes

This new kafka version does without Apache zookeeper for managing metadata

Resources for a tutorial that covers running KRaft mode Kafka v3.0.0 on a Minikube-based Kubernetes cluster.

1- Get into one of the kafka pods in namespace - kafka-kraft

```sh
kubectl exec -it kafka-0 -n kafka-kraft -- /bin/bash
# if in default namespace, below should suffice
kubectl exec -it kafka-0 -- /bin/bash
```

2- Create topic named location

```sh
kafka-topics.sh --create --topic location --partitions 3 --replication-factor 3 --bootstrap-server localhost:9092
```

3- Check the configuration

```sh
kafka-topics.sh --describe --topic location --bootstrap-server localhost:9092
```

4- Test inside the pods

```sh
kafka-console-producer.sh \
  --topic location \
  --bootstrap-server localhost:9092 #\
  #--property parse.key=true \  # optional
  #--property key.separator=":"  # optional
```

In another terminal
Console consumer:

```sh
kafka-console-consumer.sh \
  --topic location \
  --bootstrap-server localhost:9092 \
  --from-beginning #\
  # --property print.key=true \ # optional
  # --property key.separator="-" # optional
```

### connecting with services within cluster

It's okay to specify just the service name if within the same namespace as the pod/service.
if cross namespace

```sh
<service_name>.<namespace>
<service_name>.<namespace>.svc
<service_name>.<namespace>.svc.cluster.local
```

 To double-check the last two parts, use CoreDNS as sample, check its configmap:

```sh
kubectl -n kube-system get configmap coredns -o yaml
```

From here, I can see the the configuration file for CoreDNS, and could be set to e.g `cluster.local` as port of full DNS name.

## Tutorial

The tutorial for this project is available [here](https://developer.ibm.com/tutorials/kafka-in-kubernetes) on [IBM Developer](https://developer.ibm.com/) (and possibly cross-posted on other sites).

## Contents

Instructions for how to use this repo are found in the tutorial (links above).

- [docker](docker/): kafka Dockerfile and entrypoint shell script
- [kubernetes](kubernetes/): kubernetes cluster config files managed by minikube

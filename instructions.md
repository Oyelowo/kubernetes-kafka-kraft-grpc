Generate code from protobuf
`python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ protobuf/person.proto`

For  person API
`python3 -m grpc_tools.protoc -I./ --python_out=./modules/api_person/app --grpc_python_out=./modules/api_person/app/ protobuf/person.proto`

This will generate protobuf code from the .proto file into `./modules/api_person/`


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




kubectl delete deployments --all 
kubectl delete statefulsets --all
kubectl delete pods --all 
kubectl delete svc --all 

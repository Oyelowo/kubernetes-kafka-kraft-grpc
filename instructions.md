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

kubectl apply -f deployment/  



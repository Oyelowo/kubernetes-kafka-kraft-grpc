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

oyelowo/udaconnect-api-person

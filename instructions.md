Generate code from protobuf
`python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ protobuf/person.proto`

For  person API
`python3 -m grpc_tools.protoc -I./ --python_out=./modules/api_person --grpc_python_out=./modules/api_person/ protobuf/person.proto`

This will generate protobuf code from the .proto file into `./modules/api_person/`

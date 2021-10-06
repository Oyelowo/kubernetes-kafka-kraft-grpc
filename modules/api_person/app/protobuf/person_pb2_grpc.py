# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuf import person_pb2 as protobuf_dot_person__pb2


class PersonServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePerson = channel.unary_unary(
                '/api.person.PersonService/CreatePerson',
                request_serializer=protobuf_dot_person__pb2.Person.SerializeToString,
                response_deserializer=protobuf_dot_person__pb2.Person.FromString,
                )
        self.GetAllPersons = channel.unary_unary(
                '/api.person.PersonService/GetAllPersons',
                request_serializer=protobuf_dot_person__pb2.Empty.SerializeToString,
                response_deserializer=protobuf_dot_person__pb2.Persons.FromString,
                )
        self.GetPerson = channel.unary_unary(
                '/api.person.PersonService/GetPerson',
                request_serializer=protobuf_dot_person__pb2.GetPersonRequest.SerializeToString,
                response_deserializer=protobuf_dot_person__pb2.Person.FromString,
                )


class PersonServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllPersons(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPerson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePerson': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePerson,
                    request_deserializer=protobuf_dot_person__pb2.Person.FromString,
                    response_serializer=protobuf_dot_person__pb2.Person.SerializeToString,
            ),
            'GetAllPersons': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllPersons,
                    request_deserializer=protobuf_dot_person__pb2.Empty.FromString,
                    response_serializer=protobuf_dot_person__pb2.Persons.SerializeToString,
            ),
            'GetPerson': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPerson,
                    request_deserializer=protobuf_dot_person__pb2.GetPersonRequest.FromString,
                    response_serializer=protobuf_dot_person__pb2.Person.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.person.PersonService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.person.PersonService/CreatePerson',
            protobuf_dot_person__pb2.Person.SerializeToString,
            protobuf_dot_person__pb2.Person.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllPersons(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.person.PersonService/GetAllPersons',
            protobuf_dot_person__pb2.Empty.SerializeToString,
            protobuf_dot_person__pb2.Persons.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.person.PersonService/GetPerson',
            protobuf_dot_person__pb2.GetPersonRequest.SerializeToString,
            protobuf_dot_person__pb2.Person.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
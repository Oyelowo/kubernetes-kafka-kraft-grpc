# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/connection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf import person_pb2 as protobuf_dot_person__pb2
from protobuf import location_pb2 as protobuf_dot_location__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/connection.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19protobuf/connection.proto\x1a\x15protobuf/person.proto\x1a\x17protobuf/location.proto\"Z\n\nConnection\x12\"\n\x06person\x18\x01 \x01(\x0b\x32\x12.api.person.Person\x12(\n\x08location\x18\x02 \x01(\x0b\x32\x16.api.location.Location\"6\n\x12\x43onnectionResponse\x12 \n\x0b\x63onnections\x18\x01 \x03(\x0b\x32\x0b.Connection\"_\n\x14GetConnectionRequest\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\x12\x0e\n\x06meters\x18\x04 \x01(\x02\x32P\n\x11\x43onnectionService\x12;\n\rGetConnection\x12\x15.GetConnectionRequest\x1a\x13.ConnectionResponseb\x06proto3'
  ,
  dependencies=[protobuf_dot_person__pb2.DESCRIPTOR,protobuf_dot_location__pb2.DESCRIPTOR,])




_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='Connection.person', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='Connection.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=167,
)


_CONNECTIONRESPONSE = _descriptor.Descriptor(
  name='ConnectionResponse',
  full_name='ConnectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connections', full_name='ConnectionResponse.connections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=223,
)


_GETCONNECTIONREQUEST = _descriptor.Descriptor(
  name='GetConnectionRequest',
  full_name='GetConnectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='GetConnectionRequest.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='GetConnectionRequest.start_date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='GetConnectionRequest.end_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meters', full_name='GetConnectionRequest.meters', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=320,
)

_CONNECTION.fields_by_name['person'].message_type = protobuf_dot_person__pb2._PERSON
_CONNECTION.fields_by_name['location'].message_type = protobuf_dot_location__pb2._LOCATION
_CONNECTIONRESPONSE.fields_by_name['connections'].message_type = _CONNECTION
DESCRIPTOR.message_types_by_name['Connection'] = _CONNECTION
DESCRIPTOR.message_types_by_name['ConnectionResponse'] = _CONNECTIONRESPONSE
DESCRIPTOR.message_types_by_name['GetConnectionRequest'] = _GETCONNECTIONREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTION,
  '__module__' : 'protobuf.connection_pb2'
  # @@protoc_insertion_point(class_scope:Connection)
  })
_sym_db.RegisterMessage(Connection)

ConnectionResponse = _reflection.GeneratedProtocolMessageType('ConnectionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONRESPONSE,
  '__module__' : 'protobuf.connection_pb2'
  # @@protoc_insertion_point(class_scope:ConnectionResponse)
  })
_sym_db.RegisterMessage(ConnectionResponse)

GetConnectionRequest = _reflection.GeneratedProtocolMessageType('GetConnectionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCONNECTIONREQUEST,
  '__module__' : 'protobuf.connection_pb2'
  # @@protoc_insertion_point(class_scope:GetConnectionRequest)
  })
_sym_db.RegisterMessage(GetConnectionRequest)



_CONNECTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ConnectionService',
  full_name='ConnectionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=322,
  serialized_end=402,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConnection',
    full_name='ConnectionService.GetConnection',
    index=0,
    containing_service=None,
    input_type=_GETCONNECTIONREQUEST,
    output_type=_CONNECTIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONNECTIONSERVICE)

DESCRIPTOR.services_by_name['ConnectionService'] = _CONNECTIONSERVICE

# @@protoc_insertion_point(module_scope)

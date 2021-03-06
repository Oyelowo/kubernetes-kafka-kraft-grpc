# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/location.proto',
  package='api.location',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17protobuf/location.proto\x12\x0c\x61pi.location\"e\n\x08Location\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\t\x12\x10\n\x08latitude\x18\x04 \x01(\t\x12\x15\n\rcreation_time\x18\x05 \x01(\t\"f\n\x15\x43reateLocationRequest\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\t\x12\x10\n\x08latitude\x18\x03 \x01(\t\x12\x15\n\rcreation_time\x18\x04 \x01(\t\" \n\x12GetLocationRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty2\xa6\x01\n\x0fLocationService\x12J\n\x0e\x43reateLocation\x12#.api.location.CreateLocationRequest\x1a\x13.api.location.Empty\x12G\n\x0bGetLocation\x12 .api.location.GetLocationRequest\x1a\x16.api.location.Locationb\x06proto3'
)




_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='api.location.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.location.Location.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='api.location.Location.person_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='api.location.Location.longitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='api.location.Location.latitude', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='api.location.Location.creation_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=41,
  serialized_end=142,
)


_CREATELOCATIONREQUEST = _descriptor.Descriptor(
  name='CreateLocationRequest',
  full_name='api.location.CreateLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='api.location.CreateLocationRequest.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='api.location.CreateLocationRequest.longitude', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='api.location.CreateLocationRequest.latitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='api.location.CreateLocationRequest.creation_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=144,
  serialized_end=246,
)


_GETLOCATIONREQUEST = _descriptor.Descriptor(
  name='GetLocationRequest',
  full_name='api.location.GetLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.location.GetLocationRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=248,
  serialized_end=280,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='api.location.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=282,
  serialized_end=289,
)

DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['CreateLocationRequest'] = _CREATELOCATIONREQUEST
DESCRIPTOR.message_types_by_name['GetLocationRequest'] = _GETLOCATIONREQUEST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:api.location.Location)
  })
_sym_db.RegisterMessage(Location)

CreateLocationRequest = _reflection.GeneratedProtocolMessageType('CreateLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOCATIONREQUEST,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:api.location.CreateLocationRequest)
  })
_sym_db.RegisterMessage(CreateLocationRequest)

GetLocationRequest = _reflection.GeneratedProtocolMessageType('GetLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETLOCATIONREQUEST,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:api.location.GetLocationRequest)
  })
_sym_db.RegisterMessage(GetLocationRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'protobuf.location_pb2'
  # @@protoc_insertion_point(class_scope:api.location.Empty)
  })
_sym_db.RegisterMessage(Empty)



_LOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='LocationService',
  full_name='api.location.LocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=292,
  serialized_end=458,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateLocation',
    full_name='api.location.LocationService.CreateLocation',
    index=0,
    containing_service=None,
    input_type=_CREATELOCATIONREQUEST,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetLocation',
    full_name='api.location.LocationService.GetLocation',
    index=1,
    containing_service=None,
    input_type=_GETLOCATIONREQUEST,
    output_type=_LOCATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONSERVICE)

DESCRIPTOR.services_by_name['LocationService'] = _LOCATIONSERVICE

# @@protoc_insertion_point(module_scope)

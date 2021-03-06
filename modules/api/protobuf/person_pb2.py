# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/person.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/person.proto',
  package='api.person',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15protobuf/person.proto\x12\napi.person\"Q\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\"R\n\x13\x43reatePersonRequest\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\"\x1e\n\x10GetPersonRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty\".\n\x07Persons\x12#\n\x07persons\x18\x01 \x03(\x0b\x32\x12.api.person.Person2\xcc\x01\n\rPersonService\x12\x43\n\x0c\x43reatePerson\x12\x1f.api.person.CreatePersonRequest\x1a\x12.api.person.Person\x12=\n\tGetPerson\x12\x1c.api.person.GetPersonRequest\x1a\x12.api.person.Person\x12\x37\n\rGetAllPersons\x12\x11.api.person.Empty\x1a\x13.api.person.Personsb\x06proto3'
)




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='api.person.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.person.Person.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='api.person.Person.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='api.person.Person.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_name', full_name='api.person.Person.company_name', index=3,
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
  serialized_start=37,
  serialized_end=118,
)


_CREATEPERSONREQUEST = _descriptor.Descriptor(
  name='CreatePersonRequest',
  full_name='api.person.CreatePersonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='api.person.CreatePersonRequest.first_name', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='api.person.CreatePersonRequest.last_name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_name', full_name='api.person.CreatePersonRequest.company_name', index=2,
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
  serialized_start=120,
  serialized_end=202,
)


_GETPERSONREQUEST = _descriptor.Descriptor(
  name='GetPersonRequest',
  full_name='api.person.GetPersonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.person.GetPersonRequest.id', index=0,
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
  serialized_start=204,
  serialized_end=234,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='api.person.Empty',
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
  serialized_start=236,
  serialized_end=243,
)


_PERSONS = _descriptor.Descriptor(
  name='Persons',
  full_name='api.person.Persons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='persons', full_name='api.person.Persons.persons', index=0,
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
  serialized_start=245,
  serialized_end=291,
)

_PERSONS.fields_by_name['persons'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['CreatePersonRequest'] = _CREATEPERSONREQUEST
DESCRIPTOR.message_types_by_name['GetPersonRequest'] = _GETPERSONREQUEST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Persons'] = _PERSONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'protobuf.person_pb2'
  # @@protoc_insertion_point(class_scope:api.person.Person)
  })
_sym_db.RegisterMessage(Person)

CreatePersonRequest = _reflection.GeneratedProtocolMessageType('CreatePersonRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPERSONREQUEST,
  '__module__' : 'protobuf.person_pb2'
  # @@protoc_insertion_point(class_scope:api.person.CreatePersonRequest)
  })
_sym_db.RegisterMessage(CreatePersonRequest)

GetPersonRequest = _reflection.GeneratedProtocolMessageType('GetPersonRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPERSONREQUEST,
  '__module__' : 'protobuf.person_pb2'
  # @@protoc_insertion_point(class_scope:api.person.GetPersonRequest)
  })
_sym_db.RegisterMessage(GetPersonRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'protobuf.person_pb2'
  # @@protoc_insertion_point(class_scope:api.person.Empty)
  })
_sym_db.RegisterMessage(Empty)

Persons = _reflection.GeneratedProtocolMessageType('Persons', (_message.Message,), {
  'DESCRIPTOR' : _PERSONS,
  '__module__' : 'protobuf.person_pb2'
  # @@protoc_insertion_point(class_scope:api.person.Persons)
  })
_sym_db.RegisterMessage(Persons)



_PERSONSERVICE = _descriptor.ServiceDescriptor(
  name='PersonService',
  full_name='api.person.PersonService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=294,
  serialized_end=498,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreatePerson',
    full_name='api.person.PersonService.CreatePerson',
    index=0,
    containing_service=None,
    input_type=_CREATEPERSONREQUEST,
    output_type=_PERSON,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPerson',
    full_name='api.person.PersonService.GetPerson',
    index=1,
    containing_service=None,
    input_type=_GETPERSONREQUEST,
    output_type=_PERSON,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllPersons',
    full_name='api.person.PersonService.GetAllPersons',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_PERSONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERSONSERVICE)

DESCRIPTOR.services_by_name['PersonService'] = _PERSONSERVICE

# @@protoc_insertion_point(module_scope)

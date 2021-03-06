# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: semantic_sim.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='semantic_sim.proto',
  package='semantic_sim',
  syntax='proto3',
  serialized_pb=_b('\n\x12semantic_sim.proto\x12\x0csemantic_sim\"\x1e\n\x0bPingRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\tPingReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1d\n\nASRRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\x08NLPReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\x8e\x01\n\x0bSemanticSim\x12<\n\x04Ping\x12\x19.semantic_sim.PingRequest\x1a\x17.semantic_sim.PingReply\"\x00\x12\x41\n\x0b\x43ommunicate\x12\x18.semantic_sim.ASRRequest\x1a\x16.semantic_sim.NLPReply\"\x00\x42\x19\n\x17\x63om.engzo.grpc.examplesb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='semantic_sim.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='semantic_sim.PingRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=66,
)


_PINGREPLY = _descriptor.Descriptor(
  name='PingReply',
  full_name='semantic_sim.PingReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='semantic_sim.PingReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=96,
)


_ASRREQUEST = _descriptor.Descriptor(
  name='ASRRequest',
  full_name='semantic_sim.ASRRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='semantic_sim.ASRRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=127,
)


_NLPREPLY = _descriptor.Descriptor(
  name='NLPReply',
  full_name='semantic_sim.NLPReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='semantic_sim.NLPReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingReply'] = _PINGREPLY
DESCRIPTOR.message_types_by_name['ASRRequest'] = _ASRREQUEST
DESCRIPTOR.message_types_by_name['NLPReply'] = _NLPREPLY

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), dict(
  DESCRIPTOR = _PINGREQUEST,
  __module__ = 'semantic_sim_pb2'
  # @@protoc_insertion_point(class_scope:semantic_sim.PingRequest)
  ))
_sym_db.RegisterMessage(PingRequest)

PingReply = _reflection.GeneratedProtocolMessageType('PingReply', (_message.Message,), dict(
  DESCRIPTOR = _PINGREPLY,
  __module__ = 'semantic_sim_pb2'
  # @@protoc_insertion_point(class_scope:semantic_sim.PingReply)
  ))
_sym_db.RegisterMessage(PingReply)

ASRRequest = _reflection.GeneratedProtocolMessageType('ASRRequest', (_message.Message,), dict(
  DESCRIPTOR = _ASRREQUEST,
  __module__ = 'semantic_sim_pb2'
  # @@protoc_insertion_point(class_scope:semantic_sim.ASRRequest)
  ))
_sym_db.RegisterMessage(ASRRequest)

NLPReply = _reflection.GeneratedProtocolMessageType('NLPReply', (_message.Message,), dict(
  DESCRIPTOR = _NLPREPLY,
  __module__ = 'semantic_sim_pb2'
  # @@protoc_insertion_point(class_scope:semantic_sim.NLPReply)
  ))
_sym_db.RegisterMessage(NLPReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\027com.engzo.grpc.examples'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class SemanticSimStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Ping = channel.unary_unary(
        '/semantic_sim.SemanticSim/Ping',
        request_serializer=PingRequest.SerializeToString,
        response_deserializer=PingReply.FromString,
        )
    self.Communicate = channel.unary_unary(
        '/semantic_sim.SemanticSim/Communicate',
        request_serializer=ASRRequest.SerializeToString,
        response_deserializer=NLPReply.FromString,
        )


class SemanticSimServicer(object):
  """The greeting service definition.
  """

  def Ping(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Communicate(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SemanticSimServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=PingRequest.FromString,
          response_serializer=PingReply.SerializeToString,
      ),
      'Communicate': grpc.unary_unary_rpc_method_handler(
          servicer.Communicate,
          request_deserializer=ASRRequest.FromString,
          response_serializer=NLPReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'semantic_sim.SemanticSim', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaSemanticSimServicer(object):
  """The greeting service definition.
  """
  def Ping(self, request, context):
    """Sends a greeting
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def Communicate(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaSemanticSimStub(object):
  """The greeting service definition.
  """
  def Ping(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Sends a greeting
    """
    raise NotImplementedError()
  Ping.future = None
  def Communicate(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Communicate.future = None


def beta_create_SemanticSim_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('semantic_sim.SemanticSim', 'Communicate'): ASRRequest.FromString,
    ('semantic_sim.SemanticSim', 'Ping'): PingRequest.FromString,
  }
  response_serializers = {
    ('semantic_sim.SemanticSim', 'Communicate'): NLPReply.SerializeToString,
    ('semantic_sim.SemanticSim', 'Ping'): PingReply.SerializeToString,
  }
  method_implementations = {
    ('semantic_sim.SemanticSim', 'Communicate'): face_utilities.unary_unary_inline(servicer.Communicate),
    ('semantic_sim.SemanticSim', 'Ping'): face_utilities.unary_unary_inline(servicer.Ping),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_SemanticSim_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('semantic_sim.SemanticSim', 'Communicate'): ASRRequest.SerializeToString,
    ('semantic_sim.SemanticSim', 'Ping'): PingRequest.SerializeToString,
  }
  response_deserializers = {
    ('semantic_sim.SemanticSim', 'Communicate'): NLPReply.FromString,
    ('semantic_sim.SemanticSim', 'Ping'): PingReply.FromString,
  }
  cardinalities = {
    'Communicate': cardinality.Cardinality.UNARY_UNARY,
    'Ping': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'semantic_sim.SemanticSim', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)

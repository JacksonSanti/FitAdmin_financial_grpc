# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"!\n\x0ePaymentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"Y\n\x07Payment\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x0f\n\x07plan_id\x18\x03 \x01(\x05\x12\x11\n\tmethod_id\x18\x04 \x01(\x05\x12\r\n\x05total\x18\x05 \x01(\x02\",\n\x0fPaymentResponse\x12\x19\n\x07payment\x18\x01 \x03(\x0b\x32\x08.Payment\"\x1e\n\x0bPlanRequest\x12\x0f\n\x07plan_id\x18\x01 \x01(\x05\"7\n\x0cPlanResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x05\"\"\n\rMethodRequest\x12\x11\n\tmethod_id\x18\x01 \x01(\x05\"<\n\x0eMethodResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x64iscount\x18\x03 \x01(\x02\x32\x45\n\x0ePaymentService\x12\x33\n\x0eGetPaymentData\x12\x0f.PaymentRequest\x1a\x10.PaymentResponse29\n\x0bPlanService\x12*\n\x0bGetPlanData\x12\x0c.PlanRequest\x1a\r.PlanResponse2A\n\rMethodService\x12\x30\n\rGetMethodData\x12\x0e.MethodRequest\x1a\x0f.MethodResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PAYMENTREQUEST']._serialized_start=17
  _globals['_PAYMENTREQUEST']._serialized_end=50
  _globals['_PAYMENT']._serialized_start=52
  _globals['_PAYMENT']._serialized_end=141
  _globals['_PAYMENTRESPONSE']._serialized_start=143
  _globals['_PAYMENTRESPONSE']._serialized_end=187
  _globals['_PLANREQUEST']._serialized_start=189
  _globals['_PLANREQUEST']._serialized_end=219
  _globals['_PLANRESPONSE']._serialized_start=221
  _globals['_PLANRESPONSE']._serialized_end=276
  _globals['_METHODREQUEST']._serialized_start=278
  _globals['_METHODREQUEST']._serialized_end=312
  _globals['_METHODRESPONSE']._serialized_start=314
  _globals['_METHODRESPONSE']._serialized_end=374
  _globals['_PAYMENTSERVICE']._serialized_start=376
  _globals['_PAYMENTSERVICE']._serialized_end=445
  _globals['_PLANSERVICE']._serialized_start=447
  _globals['_PLANSERVICE']._serialized_end=504
  _globals['_METHODSERVICE']._serialized_start=506
  _globals['_METHODSERVICE']._serialized_end=571
# @@protoc_insertion_point(module_scope)

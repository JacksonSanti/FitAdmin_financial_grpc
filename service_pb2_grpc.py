# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import service_pb2 as service__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PaymentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPaymentData = channel.unary_unary(
                '/PaymentService/GetPaymentData',
                request_serializer=service__pb2.PaymentRequest.SerializeToString,
                response_deserializer=service__pb2.PaymentResponse.FromString,
                _registered_method=True)


class PaymentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPaymentData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PaymentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPaymentData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPaymentData,
                    request_deserializer=service__pb2.PaymentRequest.FromString,
                    response_serializer=service__pb2.PaymentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PaymentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('PaymentService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PaymentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPaymentData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PaymentService/GetPaymentData',
            service__pb2.PaymentRequest.SerializeToString,
            service__pb2.PaymentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class PlanServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPlanData = channel.unary_unary(
                '/PlanService/GetPlanData',
                request_serializer=service__pb2.PlanRequest.SerializeToString,
                response_deserializer=service__pb2.PlanResponse.FromString,
                _registered_method=True)


class PlanServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPlanData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlanServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPlanData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlanData,
                    request_deserializer=service__pb2.PlanRequest.FromString,
                    response_serializer=service__pb2.PlanResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PlanService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('PlanService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PlanService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPlanData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PlanService/GetPlanData',
            service__pb2.PlanRequest.SerializeToString,
            service__pb2.PlanResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class MethodServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMethodData = channel.unary_unary(
                '/MethodService/GetMethodData',
                request_serializer=service__pb2.MethodRequest.SerializeToString,
                response_deserializer=service__pb2.MethodResponse.FromString,
                _registered_method=True)


class MethodServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMethodData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MethodServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMethodData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMethodData,
                    request_deserializer=service__pb2.MethodRequest.FromString,
                    response_serializer=service__pb2.MethodResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MethodService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('MethodService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MethodService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMethodData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/MethodService/GetMethodData',
            service__pb2.MethodRequest.SerializeToString,
            service__pb2.MethodResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

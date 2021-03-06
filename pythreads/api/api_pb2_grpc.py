# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pythreads.api import api_pb2 as api__pb2


class APIStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NewStore = channel.unary_unary(
        '/api.pb.API/NewStore',
        request_serializer=api__pb2.NewStoreRequest.SerializeToString,
        response_deserializer=api__pb2.NewStoreReply.FromString,
        )
    self.RegisterSchema = channel.unary_unary(
        '/api.pb.API/RegisterSchema',
        request_serializer=api__pb2.RegisterSchemaRequest.SerializeToString,
        response_deserializer=api__pb2.RegisterSchemaReply.FromString,
        )
    self.Start = channel.unary_unary(
        '/api.pb.API/Start',
        request_serializer=api__pb2.StartRequest.SerializeToString,
        response_deserializer=api__pb2.StartReply.FromString,
        )
    self.StartFromAddress = channel.unary_unary(
        '/api.pb.API/StartFromAddress',
        request_serializer=api__pb2.StartFromAddressRequest.SerializeToString,
        response_deserializer=api__pb2.StartFromAddressReply.FromString,
        )
    self.GetStoreLink = channel.unary_unary(
        '/api.pb.API/GetStoreLink',
        request_serializer=api__pb2.GetStoreLinkRequest.SerializeToString,
        response_deserializer=api__pb2.GetStoreLinkReply.FromString,
        )
    self.ModelCreate = channel.unary_unary(
        '/api.pb.API/ModelCreate',
        request_serializer=api__pb2.ModelCreateRequest.SerializeToString,
        response_deserializer=api__pb2.ModelCreateReply.FromString,
        )
    self.ModelSave = channel.unary_unary(
        '/api.pb.API/ModelSave',
        request_serializer=api__pb2.ModelSaveRequest.SerializeToString,
        response_deserializer=api__pb2.ModelSaveReply.FromString,
        )
    self.ModelDelete = channel.unary_unary(
        '/api.pb.API/ModelDelete',
        request_serializer=api__pb2.ModelDeleteRequest.SerializeToString,
        response_deserializer=api__pb2.ModelDeleteReply.FromString,
        )
    self.ModelHas = channel.unary_unary(
        '/api.pb.API/ModelHas',
        request_serializer=api__pb2.ModelHasRequest.SerializeToString,
        response_deserializer=api__pb2.ModelHasReply.FromString,
        )
    self.ModelFind = channel.unary_unary(
        '/api.pb.API/ModelFind',
        request_serializer=api__pb2.ModelFindRequest.SerializeToString,
        response_deserializer=api__pb2.ModelFindReply.FromString,
        )
    self.ModelFindByID = channel.unary_unary(
        '/api.pb.API/ModelFindByID',
        request_serializer=api__pb2.ModelFindByIDRequest.SerializeToString,
        response_deserializer=api__pb2.ModelFindByIDReply.FromString,
        )
    self.ReadTransaction = channel.stream_stream(
        '/api.pb.API/ReadTransaction',
        request_serializer=api__pb2.ReadTransactionRequest.SerializeToString,
        response_deserializer=api__pb2.ReadTransactionReply.FromString,
        )
    self.WriteTransaction = channel.stream_stream(
        '/api.pb.API/WriteTransaction',
        request_serializer=api__pb2.WriteTransactionRequest.SerializeToString,
        response_deserializer=api__pb2.WriteTransactionReply.FromString,
        )
    self.Listen = channel.unary_stream(
        '/api.pb.API/Listen',
        request_serializer=api__pb2.ListenRequest.SerializeToString,
        response_deserializer=api__pb2.ListenReply.FromString,
        )


class APIServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def NewStore(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterSchema(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Start(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartFromAddress(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStoreLink(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelSave(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelHas(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelFind(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelFindByID(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReadTransaction(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteTransaction(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Listen(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NewStore': grpc.unary_unary_rpc_method_handler(
          servicer.NewStore,
          request_deserializer=api__pb2.NewStoreRequest.FromString,
          response_serializer=api__pb2.NewStoreReply.SerializeToString,
      ),
      'RegisterSchema': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterSchema,
          request_deserializer=api__pb2.RegisterSchemaRequest.FromString,
          response_serializer=api__pb2.RegisterSchemaReply.SerializeToString,
      ),
      'Start': grpc.unary_unary_rpc_method_handler(
          servicer.Start,
          request_deserializer=api__pb2.StartRequest.FromString,
          response_serializer=api__pb2.StartReply.SerializeToString,
      ),
      'StartFromAddress': grpc.unary_unary_rpc_method_handler(
          servicer.StartFromAddress,
          request_deserializer=api__pb2.StartFromAddressRequest.FromString,
          response_serializer=api__pb2.StartFromAddressReply.SerializeToString,
      ),
      'GetStoreLink': grpc.unary_unary_rpc_method_handler(
          servicer.GetStoreLink,
          request_deserializer=api__pb2.GetStoreLinkRequest.FromString,
          response_serializer=api__pb2.GetStoreLinkReply.SerializeToString,
      ),
      'ModelCreate': grpc.unary_unary_rpc_method_handler(
          servicer.ModelCreate,
          request_deserializer=api__pb2.ModelCreateRequest.FromString,
          response_serializer=api__pb2.ModelCreateReply.SerializeToString,
      ),
      'ModelSave': grpc.unary_unary_rpc_method_handler(
          servicer.ModelSave,
          request_deserializer=api__pb2.ModelSaveRequest.FromString,
          response_serializer=api__pb2.ModelSaveReply.SerializeToString,
      ),
      'ModelDelete': grpc.unary_unary_rpc_method_handler(
          servicer.ModelDelete,
          request_deserializer=api__pb2.ModelDeleteRequest.FromString,
          response_serializer=api__pb2.ModelDeleteReply.SerializeToString,
      ),
      'ModelHas': grpc.unary_unary_rpc_method_handler(
          servicer.ModelHas,
          request_deserializer=api__pb2.ModelHasRequest.FromString,
          response_serializer=api__pb2.ModelHasReply.SerializeToString,
      ),
      'ModelFind': grpc.unary_unary_rpc_method_handler(
          servicer.ModelFind,
          request_deserializer=api__pb2.ModelFindRequest.FromString,
          response_serializer=api__pb2.ModelFindReply.SerializeToString,
      ),
      'ModelFindByID': grpc.unary_unary_rpc_method_handler(
          servicer.ModelFindByID,
          request_deserializer=api__pb2.ModelFindByIDRequest.FromString,
          response_serializer=api__pb2.ModelFindByIDReply.SerializeToString,
      ),
      'ReadTransaction': grpc.stream_stream_rpc_method_handler(
          servicer.ReadTransaction,
          request_deserializer=api__pb2.ReadTransactionRequest.FromString,
          response_serializer=api__pb2.ReadTransactionReply.SerializeToString,
      ),
      'WriteTransaction': grpc.stream_stream_rpc_method_handler(
          servicer.WriteTransaction,
          request_deserializer=api__pb2.WriteTransactionRequest.FromString,
          response_serializer=api__pb2.WriteTransactionReply.SerializeToString,
      ),
      'Listen': grpc.unary_stream_rpc_method_handler(
          servicer.Listen,
          request_deserializer=api__pb2.ListenRequest.FromString,
          response_serializer=api__pb2.ListenReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'api.pb.API', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

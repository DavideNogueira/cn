# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import books_pb2 as books__pb2


class BookServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddBook = channel.unary_unary(
                '/BookService/AddBook',
                request_serializer=books__pb2.AddBookRequest.SerializeToString,
                response_deserializer=books__pb2.BookMessage.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/BookService/GetBook',
                request_serializer=books__pb2.GetBookRequest.SerializeToString,
                response_deserializer=books__pb2.Book.FromString,
                )
        self.UpdateBook = channel.unary_unary(
                '/BookService/UpdateBook',
                request_serializer=books__pb2.UpdateBookRequest.SerializeToString,
                response_deserializer=books__pb2.BookMessage.FromString,
                )
        self.DeleteBook = channel.unary_unary(
                '/BookService/DeleteBook',
                request_serializer=books__pb2.DeleteBookRequest.SerializeToString,
                response_deserializer=books__pb2.BookMessage.FromString,
                )
        self.GetBookByTitle = channel.unary_unary(
                '/BookService/GetBookByTitle',
                request_serializer=books__pb2.GetBookByTitleRequest.SerializeToString,
                response_deserializer=books__pb2.GetBookByTitleResponse.FromString,
                )


class BookServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBookByTitle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddBook': grpc.unary_unary_rpc_method_handler(
                    servicer.AddBook,
                    request_deserializer=books__pb2.AddBookRequest.FromString,
                    response_serializer=books__pb2.BookMessage.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=books__pb2.GetBookRequest.FromString,
                    response_serializer=books__pb2.Book.SerializeToString,
            ),
            'UpdateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBook,
                    request_deserializer=books__pb2.UpdateBookRequest.FromString,
                    response_serializer=books__pb2.BookMessage.SerializeToString,
            ),
            'DeleteBook': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBook,
                    request_deserializer=books__pb2.DeleteBookRequest.FromString,
                    response_serializer=books__pb2.BookMessage.SerializeToString,
            ),
            'GetBookByTitle': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBookByTitle,
                    request_deserializer=books__pb2.GetBookByTitleRequest.FromString,
                    response_serializer=books__pb2.GetBookByTitleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/AddBook',
            books__pb2.AddBookRequest.SerializeToString,
            books__pb2.BookMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/GetBook',
            books__pb2.GetBookRequest.SerializeToString,
            books__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/UpdateBook',
            books__pb2.UpdateBookRequest.SerializeToString,
            books__pb2.BookMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/DeleteBook',
            books__pb2.DeleteBookRequest.SerializeToString,
            books__pb2.BookMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBookByTitle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BookService/GetBookByTitle',
            books__pb2.GetBookByTitleRequest.SerializeToString,
            books__pb2.GetBookByTitleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
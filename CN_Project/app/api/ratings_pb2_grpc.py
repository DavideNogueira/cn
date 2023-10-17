# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ratings_pb2 as ratings__pb2


class RatingsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddRating = channel.unary_unary(
                '/RatingsService/AddRating',
                request_serializer=ratings__pb2.AddRatingRequest.SerializeToString,
                response_deserializer=ratings__pb2.RatingMessage.FromString,
                )
        self.UpdateRating = channel.unary_unary(
                '/RatingsService/UpdateRating',
                request_serializer=ratings__pb2.UpdateRatingRequest.SerializeToString,
                response_deserializer=ratings__pb2.RatingMessage.FromString,
                )
        self.DeleteRating = channel.unary_unary(
                '/RatingsService/DeleteRating',
                request_serializer=ratings__pb2.DeleteRatingRequest.SerializeToString,
                response_deserializer=ratings__pb2.RatingMessage.FromString,
                )
        self.GetRatingsByReviewScore = channel.unary_unary(
                '/RatingsService/GetRatingsByReviewScore',
                request_serializer=ratings__pb2.GetRatingsByReviewScoreRequest.SerializeToString,
                response_deserializer=ratings__pb2.GetRatingsByReviewScoreResponse.FromString,
                )
        self.GetRatingsByBookId = channel.unary_unary(
                '/RatingsService/GetRatingsByBookId',
                request_serializer=ratings__pb2.GetRatingsByBookIdRequest.SerializeToString,
                response_deserializer=ratings__pb2.GetRatingsByBookIdResponse.FromString,
                )
        self.GetRatingsByBookTitle = channel.unary_unary(
                '/RatingsService/GetRatingsByBookTitle',
                request_serializer=ratings__pb2.GetRatingsByBookTitleReuqest.SerializeToString,
                response_deserializer=ratings__pb2.GetRatingsByBookTitleResponse.FromString,
                )


class RatingsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddRating(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRating(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRating(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRatingsByReviewScore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRatingsByBookId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRatingsByBookTitle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RatingsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddRating': grpc.unary_unary_rpc_method_handler(
                    servicer.AddRating,
                    request_deserializer=ratings__pb2.AddRatingRequest.FromString,
                    response_serializer=ratings__pb2.RatingMessage.SerializeToString,
            ),
            'UpdateRating': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRating,
                    request_deserializer=ratings__pb2.UpdateRatingRequest.FromString,
                    response_serializer=ratings__pb2.RatingMessage.SerializeToString,
            ),
            'DeleteRating': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRating,
                    request_deserializer=ratings__pb2.DeleteRatingRequest.FromString,
                    response_serializer=ratings__pb2.RatingMessage.SerializeToString,
            ),
            'GetRatingsByReviewScore': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRatingsByReviewScore,
                    request_deserializer=ratings__pb2.GetRatingsByReviewScoreRequest.FromString,
                    response_serializer=ratings__pb2.GetRatingsByReviewScoreResponse.SerializeToString,
            ),
            'GetRatingsByBookId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRatingsByBookId,
                    request_deserializer=ratings__pb2.GetRatingsByBookIdRequest.FromString,
                    response_serializer=ratings__pb2.GetRatingsByBookIdResponse.SerializeToString,
            ),
            'GetRatingsByBookTitle': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRatingsByBookTitle,
                    request_deserializer=ratings__pb2.GetRatingsByBookTitleReuqest.FromString,
                    response_serializer=ratings__pb2.GetRatingsByBookTitleResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RatingsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RatingsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddRating(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RatingsService/AddRating',
            ratings__pb2.AddRatingRequest.SerializeToString,
            ratings__pb2.RatingMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRating(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RatingsService/UpdateRating',
            ratings__pb2.UpdateRatingRequest.SerializeToString,
            ratings__pb2.RatingMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRating(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RatingsService/DeleteRating',
            ratings__pb2.DeleteRatingRequest.SerializeToString,
            ratings__pb2.RatingMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRatingsByReviewScore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RatingsService/GetRatingsByReviewScore',
            ratings__pb2.GetRatingsByReviewScoreRequest.SerializeToString,
            ratings__pb2.GetRatingsByReviewScoreResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRatingsByBookId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RatingsService/GetRatingsByBookId',
            ratings__pb2.GetRatingsByBookIdRequest.SerializeToString,
            ratings__pb2.GetRatingsByBookIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRatingsByBookTitle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RatingsService/GetRatingsByBookTitle',
            ratings__pb2.GetRatingsByBookTitleReuqest.SerializeToString,
            ratings__pb2.GetRatingsByBookTitleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
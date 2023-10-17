# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ratings.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rratings.proto\"\xdd\x01\n\x06Rating\x12\n\n\x02Id\x18\x01 \x01(\t\x12\r\n\x05Title\x18\x02 \x01(\t\x12\r\n\x05Price\x18\x03 \x01(\t\x12\x0f\n\x07User_id\x18\x04 \x01(\t\x12\x13\n\x0bprofileName\x18\x05 \x01(\t\x12\x1a\n\x12review_helpfulness\x18\x06 \x01(\t\x12\x14\n\x0creview_score\x18\x07 \x01(\t\x12\x13\n\x0breview_time\x18\x08 \x01(\t\x12\x16\n\x0ereview_summary\x18\t \x01(\t\x12\x13\n\x0breview_text\x18\n \x01(\t\x12\x0f\n\x07\x62ook_id\x18\x0b \x01(\x05\"+\n\x10\x41\x64\x64RatingRequest\x12\x17\n\x06rating\x18\x01 \x01(\x0b\x32\x07.Rating\" \n\rRatingMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"A\n\x13UpdateRatingRequest\x12\x11\n\trating_id\x18\x01 \x01(\t\x12\x17\n\x06rating\x18\x02 \x01(\x0b\x32\x07.Rating\"(\n\x13\x44\x65leteRatingRequest\x12\x11\n\trating_id\x18\x01 \x01(\t\"2\n\x1cGetRatingsByBookTitleReuqest\x12\x12\n\nbook_title\x18\x01 \x01(\t\"6\n\x1eGetRatingsByReviewScoreRequest\x12\x14\n\x0creview_score\x18\x01 \x01(\t\",\n\x19GetRatingsByBookIdRequest\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\x05\"6\n\x1aGetRatingsByBookIdResponse\x12\x18\n\x07ratings\x18\x01 \x03(\x0b\x32\x07.Rating\"E\n\x1dGetRatingsBetweenDatesRequest\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x02 \x01(\t\":\n\x1eGetRatingsBetweenDatesResponse\x12\x18\n\x07ratings\x18\x01 \x03(\x0b\x32\x07.Rating\";\n\x1fGetRatingsByReviewScoreResponse\x12\x18\n\x07ratings\x18\x01 \x03(\x0b\x32\x07.Rating\"9\n\x1dGetRatingsByBookTitleResponse\x12\x18\n\x07ratings\x18\x01 \x03(\x0b\x32\x07.Rating2\xb1\x03\n\x0eRatingsService\x12.\n\tAddRating\x12\x11.AddRatingRequest\x1a\x0e.RatingMessage\x12\x34\n\x0cUpdateRating\x12\x14.UpdateRatingRequest\x1a\x0e.RatingMessage\x12\x34\n\x0c\x44\x65leteRating\x12\x14.DeleteRatingRequest\x1a\x0e.RatingMessage\x12\\\n\x17GetRatingsByReviewScore\x12\x1f.GetRatingsByReviewScoreRequest\x1a .GetRatingsByReviewScoreResponse\x12M\n\x12GetRatingsByBookId\x12\x1a.GetRatingsByBookIdRequest\x1a\x1b.GetRatingsByBookIdResponse\x12V\n\x15GetRatingsByBookTitle\x12\x1d.GetRatingsByBookTitleReuqest\x1a\x1e.GetRatingsByBookTitleResponseb\x06proto3')



_RATING = DESCRIPTOR.message_types_by_name['Rating']
_ADDRATINGREQUEST = DESCRIPTOR.message_types_by_name['AddRatingRequest']
_RATINGMESSAGE = DESCRIPTOR.message_types_by_name['RatingMessage']
_UPDATERATINGREQUEST = DESCRIPTOR.message_types_by_name['UpdateRatingRequest']
_DELETERATINGREQUEST = DESCRIPTOR.message_types_by_name['DeleteRatingRequest']
_GETRATINGSBYBOOKTITLEREUQEST = DESCRIPTOR.message_types_by_name['GetRatingsByBookTitleReuqest']
_GETRATINGSBYREVIEWSCOREREQUEST = DESCRIPTOR.message_types_by_name['GetRatingsByReviewScoreRequest']
_GETRATINGSBYBOOKIDREQUEST = DESCRIPTOR.message_types_by_name['GetRatingsByBookIdRequest']
_GETRATINGSBYBOOKIDRESPONSE = DESCRIPTOR.message_types_by_name['GetRatingsByBookIdResponse']
_GETRATINGSBETWEENDATESREQUEST = DESCRIPTOR.message_types_by_name['GetRatingsBetweenDatesRequest']
_GETRATINGSBETWEENDATESRESPONSE = DESCRIPTOR.message_types_by_name['GetRatingsBetweenDatesResponse']
_GETRATINGSBYREVIEWSCORERESPONSE = DESCRIPTOR.message_types_by_name['GetRatingsByReviewScoreResponse']
_GETRATINGSBYBOOKTITLERESPONSE = DESCRIPTOR.message_types_by_name['GetRatingsByBookTitleResponse']
Rating = _reflection.GeneratedProtocolMessageType('Rating', (_message.Message,), {
  'DESCRIPTOR' : _RATING,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:Rating)
  })
_sym_db.RegisterMessage(Rating)

AddRatingRequest = _reflection.GeneratedProtocolMessageType('AddRatingRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDRATINGREQUEST,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:AddRatingRequest)
  })
_sym_db.RegisterMessage(AddRatingRequest)

RatingMessage = _reflection.GeneratedProtocolMessageType('RatingMessage', (_message.Message,), {
  'DESCRIPTOR' : _RATINGMESSAGE,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:RatingMessage)
  })
_sym_db.RegisterMessage(RatingMessage)

UpdateRatingRequest = _reflection.GeneratedProtocolMessageType('UpdateRatingRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERATINGREQUEST,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:UpdateRatingRequest)
  })
_sym_db.RegisterMessage(UpdateRatingRequest)

DeleteRatingRequest = _reflection.GeneratedProtocolMessageType('DeleteRatingRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETERATINGREQUEST,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:DeleteRatingRequest)
  })
_sym_db.RegisterMessage(DeleteRatingRequest)

GetRatingsByBookTitleReuqest = _reflection.GeneratedProtocolMessageType('GetRatingsByBookTitleReuqest', (_message.Message,), {
  'DESCRIPTOR' : _GETRATINGSBYBOOKTITLEREUQEST,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:GetRatingsByBookTitleReuqest)
  })
_sym_db.RegisterMessage(GetRatingsByBookTitleReuqest)

GetRatingsByReviewScoreRequest = _reflection.GeneratedProtocolMessageType('GetRatingsByReviewScoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRATINGSBYREVIEWSCOREREQUEST,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:GetRatingsByReviewScoreRequest)
  })
_sym_db.RegisterMessage(GetRatingsByReviewScoreRequest)

GetRatingsByBookIdRequest = _reflection.GeneratedProtocolMessageType('GetRatingsByBookIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRATINGSBYBOOKIDREQUEST,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:GetRatingsByBookIdRequest)
  })
_sym_db.RegisterMessage(GetRatingsByBookIdRequest)

GetRatingsByBookIdResponse = _reflection.GeneratedProtocolMessageType('GetRatingsByBookIdResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRATINGSBYBOOKIDRESPONSE,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:GetRatingsByBookIdResponse)
  })
_sym_db.RegisterMessage(GetRatingsByBookIdResponse)

GetRatingsBetweenDatesRequest = _reflection.GeneratedProtocolMessageType('GetRatingsBetweenDatesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRATINGSBETWEENDATESREQUEST,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:GetRatingsBetweenDatesRequest)
  })
_sym_db.RegisterMessage(GetRatingsBetweenDatesRequest)

GetRatingsBetweenDatesResponse = _reflection.GeneratedProtocolMessageType('GetRatingsBetweenDatesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRATINGSBETWEENDATESRESPONSE,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:GetRatingsBetweenDatesResponse)
  })
_sym_db.RegisterMessage(GetRatingsBetweenDatesResponse)

GetRatingsByReviewScoreResponse = _reflection.GeneratedProtocolMessageType('GetRatingsByReviewScoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRATINGSBYREVIEWSCORERESPONSE,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:GetRatingsByReviewScoreResponse)
  })
_sym_db.RegisterMessage(GetRatingsByReviewScoreResponse)

GetRatingsByBookTitleResponse = _reflection.GeneratedProtocolMessageType('GetRatingsByBookTitleResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRATINGSBYBOOKTITLERESPONSE,
  '__module__' : 'ratings_pb2'
  # @@protoc_insertion_point(class_scope:GetRatingsByBookTitleResponse)
  })
_sym_db.RegisterMessage(GetRatingsByBookTitleResponse)

_RATINGSSERVICE = DESCRIPTOR.services_by_name['RatingsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RATING._serialized_start=18
  _RATING._serialized_end=239
  _ADDRATINGREQUEST._serialized_start=241
  _ADDRATINGREQUEST._serialized_end=284
  _RATINGMESSAGE._serialized_start=286
  _RATINGMESSAGE._serialized_end=318
  _UPDATERATINGREQUEST._serialized_start=320
  _UPDATERATINGREQUEST._serialized_end=385
  _DELETERATINGREQUEST._serialized_start=387
  _DELETERATINGREQUEST._serialized_end=427
  _GETRATINGSBYBOOKTITLEREUQEST._serialized_start=429
  _GETRATINGSBYBOOKTITLEREUQEST._serialized_end=479
  _GETRATINGSBYREVIEWSCOREREQUEST._serialized_start=481
  _GETRATINGSBYREVIEWSCOREREQUEST._serialized_end=535
  _GETRATINGSBYBOOKIDREQUEST._serialized_start=537
  _GETRATINGSBYBOOKIDREQUEST._serialized_end=581
  _GETRATINGSBYBOOKIDRESPONSE._serialized_start=583
  _GETRATINGSBYBOOKIDRESPONSE._serialized_end=637
  _GETRATINGSBETWEENDATESREQUEST._serialized_start=639
  _GETRATINGSBETWEENDATESREQUEST._serialized_end=708
  _GETRATINGSBETWEENDATESRESPONSE._serialized_start=710
  _GETRATINGSBETWEENDATESRESPONSE._serialized_end=768
  _GETRATINGSBYREVIEWSCORERESPONSE._serialized_start=770
  _GETRATINGSBYREVIEWSCORERESPONSE._serialized_end=829
  _GETRATINGSBYBOOKTITLERESPONSE._serialized_start=831
  _GETRATINGSBYBOOKTITLERESPONSE._serialized_end=888
  _RATINGSSERVICE._serialized_start=891
  _RATINGSSERVICE._serialized_end=1324
# @@protoc_insertion_point(module_scope)
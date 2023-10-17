import os
import grpc

from ratings_pb2 import *
from ratings_pb2_grpc import RatingsServiceStub

from ratings_pb2 import GetRatingsBetweenDatesRequest

#ratings_host = os.getenv("RATING_HOST", "localhost")
ratings_host = os.getenv("RATING_HOST", "10.95.128.56")
ratings_channel = grpc.insecure_channel(f"{ratings_host}:50052", options=[('grpc.max_send_message_length', 104857600), ('grpc.max_receive_message_length', 104857600)])
ratings_client = RatingsServiceStub(ratings_channel)

import lib_users
import prometheus

def post_rating(rating, token):
    prometheus.REQUESTS.inc()

    if lib_users.verifyUser(token) == "invalid":
        return 'Invalid token'
    
    rating_message = Rating(
        Id=rating["Id"],
        Title=rating["Title"],
        Price=rating["Price"],
        User_id=rating["User_id"],
        book_id=rating["book_id"],
        profileName=rating["profileName"],
        review_helpfulness=rating["review/helpfulness"],
        review_score=rating["review/score"],
        review_time=rating["review/time"],
        review_summary=rating["review/summary"],
        review_text=rating["review/text"],
    )

    request = AddRatingRequest(rating=rating_message)

    response = ratings_client.AddRating(request)
    print(response)
    return str(response)


def put_rating(rating_id, rating, token):
    prometheus.REQUESTS.inc()

    if lib_users.verify(token) == "invalid":
        return 'Invalid token'

    rating_message = Rating(
        Id=rating["Id"],
        Title=rating["Title"],
        Price=rating["Price"],
        User_id=rating["User_id"],
        profileName=rating["profileName"],
        review_helpfulness=rating["review/helpfulness"],
        review_score=rating["review/score"],
        review_time=rating["review/time"],
        review_summary=rating["review/summary"],
        review_text=rating["review/text"],
    )

    request = UpdateRatingRequest(
        rating_id=rating_id,
        rating=rating_message
    )

    response = ratings_client.UpdateRating(request)
    return str(response)


def delete_rating(rating_id, token):
    prometheus.REQUESTS.inc()

    if lib_users.verify(token) == "invalid":
        return 'Invalid token'
    request = DeleteRatingRequest(rating_id=rating_id)
    response = ratings_client.DeleteRating(request)
    return str(response)


def get_reviewByScore(review_score):
    prometheus.REQUESTS.inc()

    review_score = review_score.replace("-", "/")
    request = GetRatingsByReviewScoreRequest(review_score=review_score)
    response = ratings_client.GetRatingsByReviewScore(request)
    return str(response)


def get_bookByPrice():
    prometheus.REQUESTS.inc()
    pass


def get_ratingByBookId(book_id):
    prometheus.REQUESTS.inc()

    request = GetRatingsByBookIdRequest(book_id=book_id)
    response = ratings_client.GetRatingsByBookId(request)
    return str(response)

def get_ratings_by_book_name(book_title):
    prometheus.REQUESTS.inc()
    
    #books - buscar id
    request = GetRatingsByBookTitleReuqest(book_title=book_title)
    print("GOT IT" + str(request))
    response = ratings_client.GetRatingsByBookTitle(request)
    #id - ratings
    return str(response)


def get_ratings_between_dates(start_date, end_date):
    prometheus.REQUESTS.inc()
    pass

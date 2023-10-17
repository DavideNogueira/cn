from concurrent import futures
import os
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from pymongo import MongoClient

import ratings_pb2
import ratings_pb2_grpc

from books_pb2 import *
from books_pb2_grpc import BookServiceStub

import prometheus

#books_host = os.getenv("BOOK_HOST", "localhost")
books_host = os.getenv("BOOK_HOST", "10.95.128.55")
books_channel = grpc.insecure_channel(f"{books_host}:50051", options=[('grpc.max_send_message_length', 104857600),('grpc.max_receive_message_length', 104857600)])
books_client = BookServiceStub(books_channel)

class RatingService(ratings_pb2_grpc.RatingsServiceServicer):

    def AddRating(self, request, context):
        prometheus.REQUESTS.inc()
         
        new_rating = ratings_pb2.Rating(
            Id=request.rating.Id,
            Title=request.rating.Title,
            Price=request.rating.Price,
            User_id=request.rating.User_id,
            book_id=request.rating.book_id,
            profileName=request.rating.profileName,
            review_helpfulness=request.rating.review_helpfulness,
            review_score=request.rating.review_score,
            review_time=request.rating.review_time,
            review_summary=request.rating.review_summary,
            review_text=request.rating.review_text,
        )

        collection_rating.insert_one({
            "Id": new_rating.Id,
            "Title": new_rating.Title,
            "Price": new_rating.Price,
            "User_id": new_rating.User_id,
            "book_id": new_rating.book_id,
            "profileName": new_rating.profileName,
            "review/helpfulness": new_rating.review_helpfulness,
            "review/score": new_rating.review_score,
            "review/time": new_rating.review_time,
            "review/summary": new_rating.review_summary,
            "review/text": new_rating.review_text,
        })

        return ratings_pb2.RatingMessage(message="Rating added successfully")

    def UpdateRating(self, request, context):
        prometheus.REQUESTS.inc()

        result = collection_rating.find_one({"Id": request.rating_id})
        if not result:
            raise NotFound("Rating not found")

        update_query = {"Id": request.rating_id}
        update_data = {"$set": {
            "Title": request.rating.Title,
            "Price": request.rating.Price,
            "User_id": request.rating.User_id,
            "profileName": request.rating.profileName,
            "review/helpfulness": request.rating.review_helpfulness,
            "review/score": request.rating.review_score,
            "review/time": request.rating.review_time,
            "review/summary": request.rating.review_summary,
            "review/text": request.rating.review_text,
        }}
        collection_rating.update_one(update_query, update_data)
        return ratings_pb2.RatingMessage(message="Rating updated successfully")

    def DeleteRating(self, request, context):
        prometheus.REQUESTS.inc()

        result = collection_rating.delete_one({"Id": request.rating_id})
        if result.deleted_count == 0:
            raise NotFound("Book not found")

        return ratings_pb2.RatingMessage(message="Rating deleted successfully")

    def GetRatingsByReviewScore(self, request, context):
        prometheus.REQUESTS.inc()

        results = collection_rating.find({"review/score": request.review_score})

        ratings = []
        for result in results:
            rating = ratings_pb2.Rating(
                Id=result['Id'],
                Title=result['Title'],
                Price=result['Price'],
                User_id=result['User_id'],
                profileName=result['profileName'],
                review_helpfulness=result['review/helpfulness'],
                review_score=result['review/score'],
                review_time=result['review/time'],
                review_summary=result['review/summary'],
                review_text=result['review/text'],
                book_id=result['book_id']
            )
            ratings.append(rating)

        response = ratings_pb2.GetRatingsByReviewScoreResponse(ratings=ratings)
        return response

    def GetRatingsByBookId(self, request, context):
        prometheus.REQUESTS.inc()

        results = collection_rating.find({"book_id": request.book_id})
        print(results)
        ratings = []    
        for result in results:
            rating = ratings_pb2.Rating(
                Id=result['Id'],
                Title=result['Title'],
                Price=result['Price'],
                User_id=result['User_id'],
                profileName=result['profileName'],
                review_helpfulness=result['review/helpfulness'],
                review_score=result['review/score'],
                review_time=result['review/time'],
                review_summary=result['review/summary'],
                review_text=result['review/text'],
                book_id=result['book_id']
            )
            ratings.append(rating)

        response = ratings_pb2.GetRatingsByBookIdResponse(ratings=ratings)
        return response
    
    def GetRatingsByBookTitle(self, request, context):
        prometheus.REQUESTS.inc()
        
        request1 = GetBookByTitleRequest(title=request.book_title)
        print("CHEGOU PRIMEIRO: " + str(request1.title))
        response1 = books_client.GetBookByTitle(request1)
        print("CHEGOU RESPONSE: " + str(response1))
        results = collection_rating.find({"book_id": response1.book_id})
        ratings = []    
        for result in results:
            rating = ratings_pb2.Rating(
                Id=result['Id'],
                Title=result['Title'],
                Price=result['Price'],
                User_id=result['User_id'],
                profileName=result['profileName'],
                review_helpfulness=result['review/helpfulness'],
                review_score=result['review/score'],
                review_time=result['review/time'],
                review_summary=result['review/summary'],
                review_text=result['review/text'],
                book_id=result['book_id']
            )
            ratings.append(rating)

        response = ratings_pb2.GetRatingsByBookTitleResponse(ratings=ratings)
        return response

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         interceptors=interceptors,
                         options=[('grpc.max_receive_message_length', 104857600),
                                  ('grpc.max_send_message_length', 104857600)]
                         )
    ratings_pb2_grpc.add_RatingsServiceServicer_to_server(
        RatingService(), server
    )

    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    #client = MongoClient("mongodb://root:root@localhost:27018/?authMechanism=DEFAULT")
    #client = MongoClient("mongodb://root:root@10.105.32.218:27017/?authMechanism=DEFAULT")
    client = MongoClient("mongodb+srv://CN:dwAf9cmr7BuwxlMG@cn-project.ftfm8oe.mongodb.net/?retryWrites=true&w=majority")
    prometheus.start_prometheus() 

    db = client["CloudComputing23"]
    collection_rating = db["books_rating"]
    print("Connected to database successfully")
    serve()

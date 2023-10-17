from concurrent import futures
import os
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from pymongo import MongoClient

import users_pb2
import users_pb2_grpc

import jwt
import datetime
from functools import wraps

import prometheus

SECRET_KEY = "your_secret_key"

class UserService(users_pb2_grpc.UserServiceServicer):
    def UpdateKey(self, request, context):
        prometheus.REQUESTS.inc()

        username = request.username
        password = request.password

        collection = db["users"]

        query = {"username": username, "password": password}
        result = collection.find_one(query)
        print(result)

        if result:
             # Generate a JWT token with a payload containing the user's identity
            token = jwt.encode({"username": username}, SECRET_KEY, algorithm="HS256")
            doc_id = result["_id"]
            update_query = {"$set": {"api_key": token}}
            collection.update_one({"_id": doc_id}, update_query)
            ok_message = token
        else:
            ok_message="Password is incorrect."

        return users_pb2.UpdateResponse(ok=ok_message)
    
    def VerifyToken(self, request, context):
        prometheus.REQUESTS.inc()

        token = request.token
        collection = db["users"]

        query = {"$and":[{'api_key': token}, {'admin': 'true'}]}
        result = collection.find_one(query)

        if result:
            ok_message="valid"
        else:
            ok_message="not valid"

        return users_pb2.UpdateResponse(ok=ok_message)
    
    def VerifyUserToken(self, request, context):
        prometheus.REQUESTS.inc()

        token = request.token
        collection = db["users"]

        query = {'api_key': token}
        result = collection.find_one(query)

        if result:
            ok_message="valid"
        else:
            ok_message="not valid"

        return users_pb2.UpdateResponse(ok=ok_message)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         interceptors=interceptors,
                         options=[('grpc.max_receive_message_length', 104857600),
                                  ('grpc.max_send_message_length', 104857600)]
                         )
    users_pb2_grpc.add_UserServiceServicer_to_server(
        UserService(), server
    )

    server.add_insecure_port("[::]:50055")
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

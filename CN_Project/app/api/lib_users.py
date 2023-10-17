import os
import grpc

from flask import Flask, jsonify, request, make_response, render_template

from users_pb2 import *
from users_pb2_grpc import UserServiceStub

#users_host = os.getenv("BOOK_HOST", "localhost")
users_host = os.getenv("BOOK_HOST", "10.95.128.57")
users_channel = grpc.insecure_channel(f"{users_host}:50055", options=[('grpc.max_send_message_length', 104857600), ('grpc.max_receive_message_length', 104857600)])

user_client = UserServiceStub(users_channel)

import prometheus

def login(username,password):

    prometheus.REQUESTS.inc()

    request = UpdateRequest(username=username, password=password)
    response = user_client.UpdateKey(request)
    return str(response)
    #return str("ola")

def verify(token):

    prometheus.REQUESTS.inc()

    request = VerifyRequest(token=token)
    response = user_client.VerifyToken(request)

    if(str(response)[5]) == "v":
        response = "valido"
    else:
        response = "invalid"

    return str(response)

def verifyUser(token):

    prometheus.REQUESTS.inc()

    request = VerifyRequest(token=token)
    response = user_client.VerifyUserToken(request)

    if(str(response)[5]) == "v":
        response = "valido"
    else:
        response = "invalid"

    return str(response)


import os
import grpc

from books_pb2 import *
from books_pb2_grpc import BookServiceStub


from flask import Flask, jsonify, request, make_response, render_template

#books_host = os.getenv("BOOK_HOST", "localhost")
books_host = os.getenv("BOOK_HOST", "10.95.128.55")
books_channel = grpc.insecure_channel(f"{books_host}:50051", options=[('grpc.max_send_message_length', 104857600),   ('grpc.max_receive_message_length', 104857600)])
books_client = BookServiceStub(books_channel)


import lib_users
import prometheus

def get_book(book_id):
    prometheus.REQUESTS.inc()

    request = GetBookRequest(book_id=book_id)
    response = books_client.GetBook(request)
    return str(response)


def post_book(book, token):
    prometheus.REQUESTS.inc()

    if lib_users.verify(token) == "invalid":
        return 'Invalid token'

    book_message = Book(
        Id=book["Id"],
        Title=book["Title"],
        description=book["description"],
        authors=book["authors"],
        image=book["image"],
        previewLink=book["previewLink"],
        publisher=book["publisher"],
        publishedDate=book["publishedDate"],
        infoLink=book["infoLink"],
        categories=book["categories"],
        ratingsCount=book["ratingsCount"],
    )

    request = AddBookRequest(book=book_message)

    response = books_client.AddBook(request)
    return str(response)


def put_book(book_id, book, token):
    prometheus.REQUESTS.inc()

    if lib_users.verify(token) == "invalid":
        return 'Invalid token'

    book_message = BookNoId(
        Title=book["Title"],
        description=book["description"],
        authors=book["authors"],
        image=book["image"],
        previewLink=book["previewLink"],
        publisher=book["publisher"],
        publishedDate=book["publishedDate"],
        infoLink=book["infoLink"],
        categories=book["categories"],
        ratingsCount=book["ratingsCount"],
    )

    request = UpdateBookRequest(
        book_id=book_id,
        book=book_message,
    )

    response = books_client.UpdateBook(request)
    return str(response)


def delete_book(book_id, token):
    prometheus.REQUESTS.inc()
    
    if lib_users.verify(token) == "invalid":
        return 'Invalid token'
    
    request = DeleteBookRequest(book_id=book_id)
    response = books_client.DeleteBook(request)
    return str(response)
from concurrent import futures
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from pymongo import MongoClient

import books_pb2
import books_pb2_grpc

import prometheus

class BookService(books_pb2_grpc.BookServiceServicer):

    def GetBook(self, request, context):
        prometheus.REQUESTS.inc()

        result = collection_book.find_one({"Id": request.book_id})
        if not result:
            raise NotFound("Book not found")

        book = books_pb2.Book(
            Id=result['Id'],
            Title=result['Title'],
            description=result['description'],
            authors=result['authors'],
            image=result['image'],
            previewLink=result['previewLink'],
            publisher=result['publisher'],
            publishedDate=result['publishedDate'],
            infoLink=result['infoLink'],
            categories=result['categories'],
            ratingsCount=result['ratingsCount']
        )
        return book

    def DeleteBook(self, request, context):
        prometheus.REQUESTS.inc()

        result = collection_book.delete_one({"Id": request.book_id})
        if result.deleted_count == 0:
            raise NotFound("Book not found")

        return books_pb2.BookMessage(message="Book deleted successfully")

    def AddBook(self, request, context):
        prometheus.REQUESTS.inc()

        new_book = books_pb2.Book(
            Id=request.book.Id,
            Title=request.book.Title,
            description=request.book.description,
            authors=request.book.authors,
            image=request.book.image,
            previewLink=request.book.previewLink,
            publisher=request.book.publisher,
            publishedDate=request.book.publishedDate,
            infoLink=request.book.infoLink,
            categories=request.book.categories,
            ratingsCount=request.book.ratingsCount
        )

        collection_book.insert_one({
            "Id": new_book.Id,
            "Title": new_book.Title,
            "description": new_book.description,
            "authors": new_book.authors,
            "image": new_book.image,
            "previewLink": new_book.previewLink,
            "publisher": new_book.publisher,
            "publishedDate": new_book.publishedDate,
            "infoLink": new_book.infoLink,
            "categories": new_book.categories,
            "ratingsCount": new_book.ratingsCount
        })

        return books_pb2.BookMessage(message="Book added successfully")

    def UpdateBook(self, request, context):
        prometheus.REQUESTS.inc()

        result = collection_book.find_one({"Id": request.book_id})
        if not result:
            raise NotFound("Book not found")

        update_query = {"Id": request.book_id}
        update_data = {"$set": {
            "Title": request.book.Title,
            "description": request.book.description,
            "authors": request.book.authors,
            "image": request.book.image,
            "previewLink": request.book.previewLink,
            "publisher": request.book.publisher,
            "publishedDate": request.book.publishedDate,
            "infoLink": request.book.infoLink,
            "categories": request.book.categories,
            "ratingsCount": request.book.ratingsCount
        }}
        collection_book.update_one(update_query, update_data)
        return books_pb2.BookMessage(message="Book updated successfully")
    
    def GetBookByTitle(self, request, context):
        prometheus.REQUESTS.inc()
        
        print(request.title)
        result = collection_book.find_one({"Title": request.title})
        print(result['Id'])
        if not result:
            raise NotFound("Book not found")

        return books_pb2.GetBookByTitleResponse(book_id=result['Id'])


def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         interceptors=interceptors,
                         options=[('grpc.max_receive_message_length', 104857600),
                                  ('grpc.max_send_message_length', 104857600)]
                         )
    books_pb2_grpc.add_BookServiceServicer_to_server(
        BookService(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    #client = MongoClient("mongodb://root:root@localhost:27018/?authMechanism=DEFAULT")
    #client = MongoClient("mongodb://root:root@10.105.32.218:27017/?authMechanism=DEFAULT")
    client = MongoClient("mongodb+srv://CN:dwAf9cmr7BuwxlMG@cn-project.ftfm8oe.mongodb.net/?retryWrites=true&w=majority")
    prometheus.start_prometheus() 

    db = client["CloudComputing23"]
    collection_book = db["books_data"]
    print("Connected to database successfully")
    serve()
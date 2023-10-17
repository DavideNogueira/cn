from prometheus_client import start_http_server, Summary, Histogram, Counter
import random
import time

# Define a counter metric to track the number of requests
REQUESTS = Counter('app_requests_total', 'Total number of requests')

def start_prometheus():
    start_http_server(9090)
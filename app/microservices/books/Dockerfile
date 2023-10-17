FROM python

RUN mkdir /expose
COPY ./ /expose/
WORKDIR /expose
RUN pip3 install -r requirements.txt

EXPOSE 50051

ENTRYPOINT ["python3", "books.py"]

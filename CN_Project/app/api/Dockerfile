FROM python

RUN mkdir /expose
COPY ./ /expose/
WORKDIR /expose
RUN pip3 install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3", "api_gateway.py"]

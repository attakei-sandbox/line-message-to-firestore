FROM python:3.8-slim

RUN mkdir /app
COPY server.py requirements.txt /app/
RUN pip install -r /app/requirements.txt

WORKDIR /app
EXPOSE 8080
CMD ["/app/server.py"]
